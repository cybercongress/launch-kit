import pandas as pd
import json
from functools import reduce
from cyberpy._wallet import address_to_address


# from comm_pool_rewards import get_cp_rewards
# from delegation_rewards import get_staking_rewards
# from euler4_rewards import get_e4_rewards
# from lifetime_rewards import get_lifetime_rewards
# from load_rewards import get_load_rewards
# from relevance_rewards import get_relevance_rewards
# from takeoff_rewards import get_takeoff_rewards


FILES = [
            ('comm_pool_rewards.csv', 'comm_pool'),
            ('delegation.csv', 'delegation'),
            ('euler4_rewards.csv', 'euler-4'),
            ('lifetime_rewards.csv', 'lifetime'),
            ('load.csv', 'load'),
            ('relevance.csv', 'relevance'),
            ('takeoff.csv', 'takeoff'),
            ('port.csv', 'port'),
            ('bostrom_lifetime.csv', 'bostrom_lifetime'),
            ('investors.csv', 'investors'),
            ('inventors.csv', 'inventors')
]


def read_csv(file):
    path = './data/' + file[0]
    df = pd.read_csv(path, header=None, names=['subject', file[1]], skiprows=1)
    df['subject'] = df.apply(lambda x: address_to_address(x['subject'], prefix='bostrom'), axis=1)
    df = df.astype({file[1]: int})
    count = df.shape[0]
    sum = df[file[1]].sum()
    return df, file[1], count, sum


def get_result_df():
    dfs = [read_csv(file)[0] for file in FILES]
    df_final = reduce(lambda left, right: pd.merge(left, right, on=['subject'], how='outer'), dfs)
    df_final['sum'] = df_final.sum(axis=1)
    df_final = df_final.sort_values(by=['sum'], ascending=False)
    df_final = df_final.reset_index()
    df_final = df_final.drop('index', axis=1)
    data = [read_csv(file)[1:] for file in FILES]
    df_pivot = pd.DataFrame(data, columns=['source', 'amount', 'sum'])
    return df_final, df_pivot


# def get_all_rewards():
#     print('Getting community pool rewards...')
#     get_cp_rewards()
#     print('Getting delegation rewards...')
#     get_staking_rewards()
#     print('Getting euler-4 rewards...')
#     get_e4_rewards()
#     print('Getting lifetime rewards...')
#     get_lifetime_rewards()
#     print('Getting takeoff rewards...')
#     get_takeoff_rewards()
#     print('Getting relevance rewards... (2 hours~)')
#     get_relevance_rewards()
#     print('Getting load rewards... (5 hours~)')
#     get_load_rewards()


if __name__ == '__main__':
    # get_all_rewards()
    # print('Getting the result dataframe')
    res = get_result_df()
    res[0].to_csv('./data/final_result.csv')
    res[1].to_csv('./data/pivot_result.csv')
    print('The final result saved to csv')
    genesis_df = res[0][['subject', 'sum']].copy()
    additional_accs = [
        ('bostrom1xszmhkfjs3s00z2nvtn7evqxw3dtus6yr8e4pw', 115_935_196_057_169),
        ('bostrom1qs9w7ry45axfxjgxa4jmuhjthzfvj78sxh5p6e', 700_000_000_000_000),
        ('bostrom1ha4pw9w2qgc2ce9jwfrwrmaft5fneus58nqwev', 50_000_000_000_000)
    ]
    add_accs_df = pd.DataFrame(additional_accs, columns=['subject', 'sum'])
    genesis_df = add_accs_df.append(genesis_df, ignore_index=True)
    genesis_df.to_csv('./data/genesis_df.csv')
    print('senate', 50_761_055_960_997)
    # df = df.set_index('subject')
    # result = df.to_json(orient="index")
    # with open('data/final_result.json', 'w') as json_file:
    #     json.dump(result, json_file)
    # print('the final result converted to json')