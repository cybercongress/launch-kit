import pandas as pd
from functools import reduce
from cyberpy._wallet import address_to_address
import json
from config import *


def read_csv(file):
    path = './data/' + file[0]
    df = pd.read_csv(path)
    df = df[['subject', 'reward']]
    df['subject'] = df.apply(lambda x: address_to_address(x['subject'], prefix='bostrom'), axis=1)
    _df = df.copy()
    _df['categoty'] = file[1]
    df = df.rename(columns={'reward': file[1]}, inplace=False)
    df = df.astype({file[1]: int})
    count = df.shape[0]
    sum = df[file[1]].sum()
    return df, file[1], count, sum, _df


def get_result_df():
    dfs = [read_csv(file)[0] for file in FILES]
    df_final = reduce(lambda left, right: pd.merge(left, right, on=['subject'], how='outer'), dfs)
    df_final['sum'] = df_final.sum(axis=1)
    df_final = df_final.sort_values(by=['sum'], ascending=False)
    df_final = df_final.reset_index()
    df_final = df_final.drop('index', axis=1)
    data = [read_csv(file)[1:4] for file in FILES]
    df_pivot = pd.DataFrame(data, columns=['source', 'amount', 'sum'])
    df_categorized = pd.concat([read_csv(file)[4] for file in FILES]).reset_index(drop=True)
    return df_final, df_pivot, df_categorized


def generate_genesis(df, senate, network_genesis):
    accounts = []
    balances = []
    account_number = 0
    for index, row in df.iterrows():
        account = {
            "@type": "/cosmos.auth.v1beta1.BaseAccount",
            "account_number": str(account_number),
            "address": row['subject'],
            "pub_key": None,
            "sequence": "0"
        }
        balance = {
            "address": row['subject'],
            "coins": [
                {
                    "amount": str(int(row['sum'])),
                    "denom": BOOT_DENOM
                },
                {
                    "amount": str(int(row['sum'])),
                    "denom": CYB_DENOM
                }
            ]
        }
        account_number += 1
        accounts.append(account)
        balances.append(balance)
        network_genesis['app_state']['auth']['accounts'] = accounts
        network_genesis['app_state']['bank']['balances'] = balances
        network_genesis['app_state']['bank']['supply'] = [
            {
                "amount": str(SUPPLY),
                "denom": BOOT_DENOM
            },
            {
                "amount": str(int(SUPPLY - senate)),
                "denom": CYB_DENOM
            },
        ]
        network_genesis['app_state']['distribution']['fee_pool']['community_pool'] = [{
            "amount": str(senate),
            "denom": BOOT_DENOM
        }]
        with open('./data/genesis.json', 'w') as fp:
            json.dump(network_genesis, fp, indent=4)


res = get_result_df()
res[0].to_csv('./data/final_result.csv')
res[1].to_csv('./data/pivot_result.csv')
res[2].to_csv('./data/categorized_result.csv')
genesis_df = res[0][['subject', 'sum']].copy()
genesis_df.to_csv('./data/genesis.csv')
senate = SUPPLY - genesis_df['sum'].sum()

with open(NETWORK_GENESIS_PATH) as json_file:
    network_genesis = json.load(json_file)

generate_genesis(genesis_df, senate, network_genesis)
