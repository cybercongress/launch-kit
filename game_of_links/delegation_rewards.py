import requests
import pandas as pd


from cyberpy._wallet import address_to_address
from config import GRAPHQL_API, BLOCK_HEIGHT, STAKING_REWARD
from utils.queries import HEADERS, STAKING_ON_BLOCK


def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(GRAPHQL_API, json={'query': query}, headers=HEADERS)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_staking():
    res = run_query(STAKING_ON_BLOCK.substitute(block=BLOCK_HEIGHT))['data']['staking']
    operator_addresses = [res['operator_address'] for res in res]
    tokens = [res['tokens'] for res in res]
    return operator_addresses, tokens


def get_staking_rewards():
    staking = get_staking()
    df = pd.DataFrame()
    df['subject'], df['tokens'] = staking
    df['reward'] = (df['tokens']/sum(df['tokens'])) * STAKING_REWARD
    df['reward'] = df['reward'].round(0)
    df['subject'] = df.apply(lambda row: address_to_address(row['subject'], 'cyber'), axis=1)
    df = df[['subject', 'reward']]
    df = df.sort_values(by=['reward'], ascending=False)
    df = df.reset_index(drop=True)
    df.to_csv('./data/delegation.csv')


