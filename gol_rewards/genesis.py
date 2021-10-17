import json
import pandas as pd

with open('./data/genesis5upd1.json') as json_file:
    genesis_network = json.load(json_file)

genesis_df = pd.read_csv('./data/genesis_df.csv')
senate = 50761055960997

accounts = []
balances = []

account_number = 0

for index, row in genesis_df.iterrows():
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
                "denom": "boot"
            }
        ]
    }
    account_number += 1
    accounts.append(account)
    balances.append(balance)


genesis_network['app_state']['auth']['accounts'] = accounts
genesis_network['app_state']['bank']['balances'] = balances
genesis_network['app_state']['bank']['supply'] = [{
                                                    "amount": "1000000000000000",
                                                    "denom": "boot"
                                                }]


genesis_network['app_state']['distribution']['fee_pool']['community_pool'] = [{
                                                                                "amount": str(senate),
                                                                                "denom": "boot"
                                                                            }]

with open('./data/genesis.json', 'w') as fp:
    json.dump(genesis_network, fp, indent=4)