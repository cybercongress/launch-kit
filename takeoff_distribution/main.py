import requests
import pandas as pd
import numpy as np
import json
from cyberpy._wallet import address_to_address
import math

from web3 import Web3
from config import *

def get_evangelist(memo):
    evangelist = ''
    if 'thanks to' in memo:
        evangelist = memo[10:]
    elif ' ' not in memo:
        evangelist = memo
    else:
        pass
    return evangelist

def evangelist_address(evangelist):
    if evangelist != '':
        return evangelists[evangelist]
    else:
        pass

def get_w3_client():
    return Web3(Web3.HTTPProvider(ETH_NODE_RPC))


def get_contract(address, abi):
    web3 = get_w3_client()
    return web3.eth.contract(address=address, abi=abi)

pages = int(requests.get(URL.format(CONGRESS_COSMOS_ADDRESS ,'1')).json()['page_total'])
contract = get_contract(EVANGELISM_CONTRACT, EVANGELISM_CONTRACT_ABI)

evangelists = {}
i = 0
while True:
    try:
        evangelist = contract.functions.evangelists(i).call()
        evangelists.update({evangelist[3]: evangelist[1]})
        i += 1
    except:
        break

txs = []

for page in range(1, pages + 1):
    resp = requests.get(URL.format(CONGRESS_COSMOS_ADDRESS, str(page))).json()
    txs.extend(resp['txs'])

timestamps = []
txshashes = []
donors = []
memos = []
donates = []

for tx in txs:
    timestamps.append(tx['timestamp'])
    txshashes.append(tx['txhash'])
    donors.append(tx['tx']['value']['msg'][0]['value']['from_address'])
    donates.append(tx['tx']['value']['msg'][0]['value']['amount'][0]['amount'])
    memos.append(tx['tx']['value']['memo'])

data = {
    'timestamps' : timestamps,
    'txshashes' : txshashes,
    'donors' : donors,
    'donates': donates,
    'memos' : memos
}

df = pd.DataFrame (data, columns = ['timestamps', 'txshashes', 'donors', 'donates', 'memos'])

df['timestamps'] = pd.to_datetime(df['timestamps'])
df = df[(df['timestamps'] > from_date) & (df['timestamps'] < to_date)]

df['donates'] = df['donates'].astype(int)
df['share'] = df['donates']/df.donates.sum()
df['distribution'] = np.round(df['share'] * takeoff_distr).astype(int)
df['evangelist'] = df.apply(lambda row: get_evangelist(row['memos']), axis=1)
df['evangelist_address'] = df.apply(lambda row: evangelist_address(row['evangelist']), axis=1)
df['cashback'] = (df['donates'] * 0.1).astype(int)
df.to_csv('./data/distribution.csv')

takeoff_df = df[['donors', 'distribution']].copy()
takeoff_df = takeoff_df.groupby(['donors']).sum().sort_values(by=['distribution'], ascending=False).reset_index()
takeoff_df.to_csv('./data/takeoff.csv')
takeoff_df['donors'] = takeoff_df.apply(lambda row: address_to_address(row['donors'], 'cyber'), axis=1)
takeoff_df.to_csv('./data/cyber.csv')

cashback_df = df[['evangelist', 'evangelist_address', 'cashback']].copy()
cashback_df = cashback_df.groupby(['evangelist', 'evangelist_address']).sum().sort_values(by=['cashback'], ascending=False).reset_index()
cashback_df.to_csv('./data/cashback.csv')

team_data = dict(zip(TEAM, ([int(round(df.donates.sum() * 0.02) / 4)] * 4)))
team_df = pd.DataFrame.from_dict(team_data, orient='index').reset_index()
team_df = team_df.rename(columns={'index': 'evangelist_address', 0: 'cashback'})
team_df.to_csv('./data/team.csv')

cashback_df = cashback_df.drop(columns=['evangelist'])
cashback_df = pd.concat([cashback_df, team_df], ignore_index=True)
cashback_df = cashback_df.groupby(['evangelist_address']).sum().sort_values(by=['cashback'], ascending=False).reset_index()
cashback_df.to_csv('./data/cosmos.csv')

# cyber tansaction preparation

msgs = []

for index, row in takeoff_df.iterrows():
    msg = {
        "type": "cosmos-sdk/MsgSend",
        "value": {
            "from_address": CONGRESS_CYBER_ADDRESS,
            "to_address": row['donors'],
            "amount": [
                {
                    "denom": "eul",
                    "amount": str(row['distribution'])
                }
            ]
        }
    }
    msgs.append(msg)

tx = {
    "type": "cosmos-sdk/StdTx",
    "value": {
        "msg": msgs,
        "fee": {
            "amount": [],
            "gas": "200000"
        },
        "signatures": None,
        "memo": "takeoff EUL distribution"
    }
}

with open("./data/cyber.json", "w") as fp:
    json.dump(tx,fp, indent=4)


# cosmos tansaction preparation

msgs = []

for index, row in cashback_df.iterrows():
    msg = {
        "type": "cosmos-sdk/MsgSend",
        "value": {
            "from_address": CONGRESS_COSMOS_ADDRESS,
            "to_address": row['evangelist_address'],
            "amount": [
                {
                    "denom": "uatom",
                    "amount": str(row['cashback'])
                }
            ]
        }
    }
    msgs.append(msg)

tx = {
    "type": "cosmos-sdk/StdTx",
    "value": {
        "msg": msgs,
        "fee": {
            "amount": [],
            "gas": "2000000"
        },
        "signatures": None,
        "memo": "evangelism cashback program and team distribution"
    }
}

with open("./data/cosmos.json", "w") as fp:
    json.dump(tx,fp, indent=4)

# print(takeoff_df.distribution.sum(), 'EULs allocated, or:', takeoff_df.distribution.sum()/1000000000000, 'TEULs')
# print(cashback_df.cashback.sum(), 'cashback uATOMs, or:', cashback_df.cashback.sum()/1000000, 'ATOMs')
# print(df.donates.sum(), 'donations uATOMs, or:', df.donates.sum()/1000000, 'ATOMs')

donates_in_atom = df.donates.sum()/1000000
donates_in_atom_ratio = donates_in_atom/300000*100
gcybs_won = (math.sqrt(5) * math.sqrt(df.donates.sum()/1000000 + 12500) - 250) / 10 * 1000
part_addresses = takeoff_df.shape[0]
disc_alloc = donates_in_atom_ratio/100 * 38 * 1000

print(' -', donates_in_atom, 'ATOMs of 300,000 have been donated and this is', donates_in_atom_ratio, '% of desirable')
print(' -', part_addresses, 'cosmos addresses participated in the takeoff and won', gcybs_won, 'GCYBs of 100000')
print(' -', 'Also, this', part_addresses, 'addresses won', disc_alloc, 'GCYBs of 38000 for Game of Links players in disciplines depends on takeoff')
print('In details:')
print(' - relevance:', 20000 * donates_in_atom_ratio/100, 'GCYBs')
print(' - load:', 10000 * donates_in_atom_ratio/100, 'GCYBs')
print(' - delegation:', 5000 * donates_in_atom_ratio/100, 'GCYBs')
print(' - lifetime:', 3000 * donates_in_atom_ratio/100, 'GCYBs')