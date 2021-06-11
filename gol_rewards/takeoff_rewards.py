import requests
import pandas as pd


from cyberpy._wallet import address_to_address
from config import COSMOSHUB_3_LCD, CONGRESS_COSMOS_ADDRESS


def get_txs():
    url = COSMOSHUB_3_LCD + f'/txs?message.action=send&transfer.recipient={CONGRESS_COSMOS_ADDRESS}&limit=30'
    pages = int(requests.get(url).json()['page_total'])
    result = []
    for page in range(pages):
        page += 1
        url = COSMOSHUB_3_LCD + f'/txs?message.action=send&transfer.recipient={CONGRESS_COSMOS_ADDRESS}&limit=30&page={page}'
        res = requests.get(url).json()
        _result = [(tx['timestamp'],
                  tx['tx']['value']['msg'][0]['value']['from_address'],
                  int(tx['tx']['value']['msg'][0]['value']['amount'][0]['amount']))
                  for tx in res['txs']]
        result.extend(_result)
    df = pd.DataFrame(result, columns=['timestamp', 'donor', 'donation'])
    df['donation'] = df['donation'] / 1_000_000
    return df


def get_tokens(atoms):
    return (1 + 50000 * 1 + 50000 * atoms + 625000000)**(1/2) - 25000


def get_price(tokens):
    return 4e-05 * tokens + 1


def get_takeoff_rewards():
    df = get_txs()
    df['cumsum'] = df['donation'].cumsum()
    for i in range(len(df)):
        df.loc[i, 'a_tokens'] = get_tokens(df.loc[i, 'cumsum'])
        df.loc[i, 'price'] = get_price(df.loc[i, 'a_tokens'])
        if i == 0:
            df.loc[i, 'reward'] = df.loc[i, 'a_tokens']
        else:
            df.loc[i, 'reward'] = df.loc[i, 'a_tokens'] - df.loc[i - 1, 'a_tokens']
    df['reward'] = df['reward'] * 1_000_000_000
    df['reward'] = df['reward'].round(0)
    df['subject'] = df.apply(lambda x: address_to_address(x['donor'], 'cyber'), axis=1)
    df = df.drop(['timestamp', 'donation', 'cumsum', 'a_tokens', 'price', 'donor'], axis=1)
    df = df.groupby(['subject']).sum()
    df = df.sort_values(by=['reward'], ascending=False)
    df = df.reset_index()
    df.to_csv('./data/takeoff.csv')
    return df