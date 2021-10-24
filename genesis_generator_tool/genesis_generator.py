import pandas as pd
from functools import reduce
from cyberpy._wallet import address_to_address
import json
from config import *


def read_csv(file):
    path = './data/' + file[0]
    df = pd.read_csv(path)
    df['subject'] = df.apply(lambda x: address_to_address(x['subject'], prefix='bostrom'), axis=1)
    _df = df.copy()
    df = df[['subject', 'reward']]
    _df['discipline'] = file[1]
    _df = _df[['subject', 'reward', 'discipline', 'audience']]
    df = df.rename(columns={'reward': file[1]}, inplace=False)
    df = df.astype({file[1]: int})
    count = df.shape[0]
    sum = df[file[1]].sum()
    return df, file[1], count, sum, _df


def get_result_df():
    dfs = [read_csv(file)[0] for file in FILES]
    df_final = reduce(lambda left, right: pd.merge(left, right, on=['subject'], how='outer'), dfs)
    df_final = df_final.groupby('subject', as_index=False).sum()
    df_final['sum'] = df_final.sum(axis=1)
    df_final = df_final.sort_values(by=['sum'], ascending=False)
    df_final = df_final.reset_index(drop=True)
    data = [read_csv(file)[1:4] for file in FILES]
    df_pivot = pd.DataFrame(data, columns=['source', 'amount', 'sum'])
    df_categorized = pd.concat([read_csv(file)[4] for file in FILES]).reset_index(drop=True)
    return df_final, df_pivot, df_categorized


def genesis_balance_checker(genesis: dict):
    balances = genesis['app_state']['bank']['balances']
    sum_boot_balances = sum([int(balance['coins'][0]['amount']) for balance in balances])
    sum_tocyb_balances = sum([int(balance['coins'][1]['amount']) for balance in balances])
    if sum_boot_balances == SUPPLY:
        print(f'boot supply is correct = {sum_boot_balances}')
    else:
        print(f'error in boot supply. Expected={SUPPLY}, got={sum_boot_balances}')
    if sum_tocyb_balances == SUPPLY:
        print(f'tocyb supply is correct = {sum_tocyb_balances}')
    else:
        print(f'error in tocyb supply. Expected={SUPPLY}, got={sum_tocyb_balances}')


def generate_genesis(df, network_genesis):
    accounts = []
    balances = []
    account_number = 0
    for index, row in df.iterrows():
        if row['subject'] != COMMUNITY_POOL_ACC:
            account = get_base_account(str(account_number), row['subject'])
            balance = get_base_balance(row['subject'], str(int(row['sum'])))
        else:
            account = get_module_account(str(account_number), row['subject'])
            balance = get_base_balance(row['subject'], str(int(row['sum'])))
        account_number += 1
        accounts.append(account)
        balances.append(balance)
    network_genesis['app_state']['auth']['accounts'] = accounts
    network_genesis['app_state']['bank']['balances'] = balances
    network_genesis['app_state']['bank']['supply'] = [
        {
            "amount": str(int(SUPPLY)),
            "denom": BOOT_DENOM
        },
        {
            "amount": str(int(SUPPLY)),
            "denom": CYB_DENOM
        },
    ]
    senate_balance = df.loc[df['subject'] == COMMUNITY_POOL_ACC].sum()[1]
    network_genesis['app_state']['distribution']['fee_pool']['community_pool'] = [
        {
            "amount": str(int(senate_balance)),
            "denom": BOOT_DENOM
        },
        {
            "amount": str(int(senate_balance)),
            "denom": CYB_DENOM
        }
    ]
    genesis_balance_checker(network_genesis)
    with open('./data/genesis.json', 'w') as fp:
        json.dump(network_genesis, fp, indent=4)


res = get_result_df()
res[0].to_csv('./data/final_result.csv')
res[1].to_csv('./data/pivot_result.csv')
res[2].to_csv('./data/categorized_result.csv')
_df = res[2].groupby(['audience', 'subject'], as_index=False)['reward'].agg(['sum'])
audience_pivot_df = _df.groupby('audience', as_index=False)['sum'].agg(['sum', 'count'])
audience_pivot_df['%'] = audience_pivot_df['sum'] / 10_000_000_000_000
audience_pivot_df.to_csv('./data/audience_pivot.csv')
discipline_pivot_df = res[2].groupby('discipline', as_index=False)['reward'].agg(['sum', 'count'])
discipline_pivot_df.to_csv('./data/discipline_pivot.csv')
genesis_df = res[0][['subject', 'sum']].copy()
genesis_df.to_csv('./data/genesis.csv')

with open(NETWORK_GENESIS_PATH) as json_file:
    network_genesis = json.load(json_file)

generate_genesis(genesis_df, network_genesis)
