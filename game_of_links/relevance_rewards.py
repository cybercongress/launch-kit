import requests
import pandas as pd
import asyncio
import aiohttp

from config import GRAPHQL_API, BLOCK_HEIGHT, IPFS_GATEWAYS, CYBER_LCD, DENOMINATORS, RELEVANCE_REWARD
from utils.queries import HEADERS, TOP_1000_ON_BLOCK


def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(GRAPHQL_API, json={'query': query}, headers=HEADERS)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_top1000():
    res = run_query(TOP_1000_ON_BLOCK.substitute(block=BLOCK_HEIGHT))['data']['relevance']
    cids = [res['object'] for res in res]
    ranks = [res['rank'] for res in res]
    return cids, ranks


DF = pd.DataFrame(columns=['particle', 'status', 'rank'])
DF['particle'], DF['rank'] = get_top1000()
DF['status'] = False


async def fetch(session, cid, gw):
    url = gw + f'/{cid}'
    try:
        async with session.get(url) as response:
            print(f'{cid}: {response.status}')
            DF.loc[DF['particle'] == cid, 'status'] = response.status
    except:
        print(f'{cid}: passed')
        pass


async def fetch_all(urls, loop, gw):
    timeout = aiohttp.ClientTimeout(total=300)
    async with aiohttp.ClientSession(loop=loop, timeout=timeout) as session:
        print('-------------------', len(urls))
        await asyncio.gather(*[fetch(session, url, gw) for url in urls], return_exceptions=False)


def processor(gw):
    cids = DF.query("status != 200")['particle'].tolist()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all(cids, loop, gw))


def get_txs_by_cid_place(cid, place):
    res = requests.get(CYBER_LCD +
                         f"/txs?message.action=link&page=1&" +
                         f"limit=30&" +
                         f"tx.maxheight={BLOCK_HEIGHT}&" +
                         f"cyberlink.{place}={cid}").json()
    pages = int(res['page_total'])
    txs = [requests.get(CYBER_LCD +
                         f"/txs?message.action=link&page={p + 1}&" +
                         f"limit=30&" +
                         f"tx.maxheight={BLOCK_HEIGHT}&" +
                         f"cyberlink.{place}={cid}").json()['txs'] for p in range(pages)]
    return [item for sublist in txs for item in sublist]


def get_agent_from_tx(tx):
    return int(tx['height']), tx['logs'][0]['events'][1]['attributes'][0]['value']


def get_shares_by_agents(df):
    agents_number = df.shape[0]
    denomenator = DENOMINATORS[agents_number - 1]
    shares = [1 / (i * denomenator) for i in range(1, agents_number + 1)]
    df['shares'] = shares
    return df


def get_agents_df(agents):
    df = pd.DataFrame(agents, columns=['height', 'subject'])
    df = df.sort_values(by=['height'])
    df = df.drop_duplicates(subset=['subject'])
    df = df.reset_index(drop=True)
    df = df[:10]
    return df


def get_agents_rewards_per_cid(cid, share):
    queries = ['objectFrom', 'objectTo']
    ress = [get_txs_by_cid_place(cid, q) for q in queries]
    txs = [item for sublist in ress for item in sublist]
    agents = [get_agent_from_tx(tx) for tx in txs]
    df = get_agents_df(agents)
    df = get_shares_by_agents(df)
    df['reward'] = share * df['shares']
    df['reward'] = df['reward'].round(0)
    print(df)
    return df


def get_rewards(df):
    _df = pd.DataFrame()
    for index, row in df.iterrows():
        print(row['particle'])
        temp_df = get_agents_rewards_per_cid(row['particle'], row['cid_share'])
        _df = _df.append(temp_df)
    return _df


def ipfs_availability_cheker():
    for i in range(5):
        print(f'stage {i}')
        for gw in IPFS_GATEWAYS:
            print(gw)
            processor(gw)
            print("Amount of particles with available content:", DF.loc[DF['status'] == 200].shape[0])
        DF.to_csv('./data/responces.csv')
    df = DF.copy()
    df = df.drop(df[df.status != 200].index)
    df['cid_share'] = (df['rank'] / sum(df['rank'])) * RELEVANCE_REWARD
    return df

def get_relevance_rewards():
    df = ipfs_availability_cheker()
    df = get_rewards(df)
    df = df.reset_index(drop=True)
    df = df[['subject', 'reward']]
    df = df.groupby(['subject']).sum()
    df = df.sort_values(by=['reward'], ascending=False)
    df.to_csv('./relevance.csv')