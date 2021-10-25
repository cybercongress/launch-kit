import pandas as pd
from cyberpy._wallet import address_to_address
import json
from config import *


def read_csv(file):
    df = pd.read_csv(file[0])
    df['subject'] = df.apply(lambda x: address_to_address(x['subject'], prefix='bostrom'), axis=1)
    if 'discipline' in list(df.columns):
        pass
    else:
        df['discipline'] = file[1]
    _df = df[['subject', 'reward', 'discipline', 'audience']]
    return _df


def get_result_df():
    return pd.concat([read_csv(file) for file in FILES]).reset_index(drop=True)


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
    with open(RESULTS_PATH + 'genesis.json', 'w') as fp:
        json.dump(network_genesis, fp, indent=4)


res = get_result_df()
res.to_csv(RESULTS_PATH + 'categorized_result.csv')
_df = res.groupby(['audience', 'subject'], as_index=False)['reward'].agg(['sum'])
audience_pivot_df = _df.groupby('audience', as_index=False)['sum'].agg(['sum', 'count'])
audience_pivot_df['%'] = audience_pivot_df['sum'] / 10_000_000_000_000
audience_pivot_df.to_csv(RESULTS_PATH + 'audience_pivot.csv')
genesis_df = res[['subject', 'reward']].copy()
genesis_df = genesis_df.groupby('subject', sort=False, as_index=False).agg('sum')
genesis_df = genesis_df.rename(columns={'reward': 'sum'}, inplace=False)
df = res.pivot(index='subject', columns='discipline', values='reward')
df['sum'] = df.sum(axis=1)
df = df.sort_values(by='sum', ascending=False)
df.to_csv(RESULTS_PATH + 'final_result.csv')
df_json = df.apply(lambda x: [x.dropna()], axis=1).to_json()
df_json = json.loads(df_json)
df_json = {key: value[0] for (key,value) in df_json.items()}
with open(RESULTS_PATH + 'genesis_app.json', 'w') as fp:
    json.dump(df_json, fp, indent=4)


with open(NETWORK_GENESIS_PATH) as json_file:
    network_genesis = json.load(json_file)

generate_genesis(genesis_df, network_genesis)
