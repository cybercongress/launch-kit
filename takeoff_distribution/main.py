import requests
import pandas as pd
import numpy as np

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

# w3 = Web3(Web3.HTTPProvider('https://mars.cybernode.ai/geth/'))

pages = int(requests.get(URL.format('1')).json()['page_total'])
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
    resp = requests.get(URL.format(str(page))).json()
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

takeoff_df = df[['donors', 'distribution']].copy()
cashback_df = df[['evangelist', 'evangelist_address', 'cashback']].copy()

takeoff_df = takeoff_df.groupby(['donors']).sum().sort_values(by=['distribution'], ascending=False)
cashback_df = cashback_df.groupby(['evangelist', 'evangelist_address']).sum().sort_values(by=['cashback'], ascending=False)

print(takeoff_df.distribution.sum(), 'EULs allocated, or:', takeoff_df.distribution.sum()/1000000000000, 'TEULs')
print(cashback_df.cashback.sum(), 'cashback uATOMs, or:', cashback_df.cashback.sum()/1000000, 'ATOMs')



df.to_csv('/Users/alpuchilo/Documents/GitHub/launch-kit/takeoff_distribution/distribution.csv')
takeoff_df.to_csv('/Users/alpuchilo/Documents/GitHub/launch-kit/takeoff_distribution/takeoff.csv')
cashback_df.to_csv('/Users/alpuchilo/Documents/GitHub/launch-kit/takeoff_distribution/cashback.csv')