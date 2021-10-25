import requests
import pandas as pd


from cyberpy._wallet import address_to_address
from config import GRAPHQL_API, LIFETIME_REWARD, CYBER_LCD
from utils.queries import HEADERS, PRECOMMITS_ON_BLOCK


def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(GRAPHQL_API, json={'query': query}, headers=HEADERS)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_precommits():
    res = run_query(PRECOMMITS_ON_BLOCK)['data']['pre_commits_final']
    consensus_pubkey = [res['consensus_pubkey'] for res in res]
    precommits = [res['precommits'] for res in res]
    return consensus_pubkey, precommits


def get_validators():
    statuses = ['bonded', 'unbonded', 'unbonding']
    final_result = []
    for status in statuses:
        result = requests.get(f"{CYBER_LCD}/staking/validators?page=1&status={status}").json()['result']
        validators = [{"operator_address": x['operator_address'], "consensus_pubkey": x['consensus_pubkey']} for x in result]
        final_result.extend(validators)
    return final_result


def get_mapped_df():
    hasura_df = pd.DataFrame(columns=['consensus_pubkey', 'precommits'])
    hasura_df['consensus_pubkey'], hasura_df['precommits'] = get_precommits()
    lcd_df = pd.DataFrame(get_validators())
    result = pd.merge(hasura_df, lcd_df, on="consensus_pubkey")
    result = result.drop(['consensus_pubkey'], axis=1)
    return result


def get_old_precommits():
    df = pd.read_csv('data/old_pre_commits.csv', header=None,
                     names=['consensus_pubkey', 'precommits', 'operator_address'],
                     usecols=['operator_address', 'precommits'])
    return df


def get_lifetime_rewards():
    e6_precommits_df = get_mapped_df()
    e5_precommits_df = get_old_precommits()
    result = pd.concat([e6_precommits_df, e5_precommits_df]).groupby(['operator_address']).sum().reset_index()
    result['subject'] = result.apply(lambda row: address_to_address(row['operator_address'], 'cyber'), axis=1)
    result['reward'] = (result['precommits'] / sum(result['precommits'])) * LIFETIME_REWARD
    result['reward'] = result['reward'].round(0)
    result = result.sort_values(by=['reward'], ascending=False)
    result = result.reset_index(drop=True)
    result = result.drop(['operator_address', 'precommits'], axis=1)
    result.to_csv('./lifetime_rewards.csv')