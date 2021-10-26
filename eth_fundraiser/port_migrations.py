import requests
import pandas as pd


from config import GRAPHQL_API, HEADERS, QUERY



def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(GRAPHQL_API, json={'query': query}, headers=HEADERS)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_port_rewards():
    r = run_query(QUERY)
    rewards = [(tx['cyber'], tx['eul']) for tx in r['data']['txs_queue']]
    df = pd.DataFrame(rewards, columns=['subject', 'reward'])
    df = df.groupby(by=['subject']).sum()
    df = df.sort_values(by=['reward'], ascending=False)
    df = df.reset_index()
    df.to_csv('./port.csv')
