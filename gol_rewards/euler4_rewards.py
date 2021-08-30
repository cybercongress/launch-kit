import pandas as pd


from cyberpy._wallet import address_to_address


def get_e4_rewards():
    df = pd.read_csv('data/euler4_raw.csv', header=None, names=['operator_address', 'reward'], skiprows=1)
    df['subject'] = df.apply(lambda x: address_to_address(x['operator_address'], 'cyber'), axis=1)
    df = df.drop(['operator_address'], axis=1)
    df = df.reindex(columns=['subject', 'reward'])
    df.to_csv('./data/euler4_rewards.csv')
