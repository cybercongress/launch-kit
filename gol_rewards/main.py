import pandas as pd
import json
from functools import reduce


from comm_pool_rewards import get_cp_rewards
from delegation_rewards import get_staking_rewards
from euler4_rewards import get_e4_rewards
from lifetime_rewards import get_lifetime_rewards
from load_rewards import get_load_rewards
from relevance_rewards import get_relevance_rewards
from takeoff_rewards import get_takeoff_rewards


FILES = [
            ('comm_pool_rewards.csv', 'comm_pool'),
            ('delegation.csv', 'delegation'),
            ('euler4_rewards.csv', 'euler-4'),
            ('lifetime_rewards.csv', 'lifetime'),
            ('load.csv', 'load'),
            ('relevance.csv', 'relevance'),
            ('takeoff.csv', 'takeoff')
]


def read_csv(file):
    path = './data/' + file[0]
    return pd.read_csv(path, header=None, names=['subject', file[1]], skiprows=1)


def get_result_df():
    dfs = [read_csv(file) for file in FILES]
    df_final = reduce(lambda left, right: pd.merge(left, right, on=['subject'], how='outer'), dfs)
    df_final['sum'] = df_final.sum(axis=1)
    df_final = df_final.sort_values(by=['sum'], ascending=False)
    df_final = df_final.reset_index()
    df_final = df_final.drop('index', axis=1)
    df_final.to_csv('./data/final_result.csv')
    return df_final


def get_all_rewards():
    print('Getting community pool rewards...')
    get_cp_rewards()
    print('Getting delegation rewards...')
    get_staking_rewards()
    print('Getting euler-4 rewards...')
    get_e4_rewards()
    print('Getting lifetime rewards...')
    get_lifetime_rewards()
    print('Getting takeoff rewards...')
    get_takeoff_rewards()
    print('Getting relevance rewards... (2 hours~)')
    get_relevance_rewards()
    print('Getting load rewards... (5 hours~)')
    get_load_rewards()


if __name__ == '__main__':
    get_all_rewards()
    print('Getting the result dataframe')
    df = get_result_df()
    print('The final result saved to csv')
    df = df.set_index('subject')
    result = df.to_json(orient="index")
    with open('./data/final_result.json', 'w') as json_file:
        json.dump(result, json_file)
    print('the final result converted to json')