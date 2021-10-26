import pandas as pd
import numpy as np
from cyberpy._wallet import address_to_address

df = pd.read_csv('data/distribution.csv')
df = df[['timestamps', 'donors', 'donates']].copy()

df['donates'] = df['donates'] / 1_000_000
df['cumsum'] = df.cumsum()['donates']
df['a_cybs'] = np.nan
df['cybs'] = np.nan
df['price'] = np.nan


def get_cybs(atoms):
    return (1 + 50000 * 1 + 50000 * atoms + 625000000)**(1/2) - 25000


def get_price(cybs):
    return 4e-05 * cybs + 1


for i in range(len(df)):
    df.loc[i, 'a_cybs'] = get_cybs(df.loc[i, 'cumsum'])
    df.loc[i, 'price'] = get_price(df.loc[i, 'a_cybs'])
    if i ==0:
        df.loc[i, 'cybs'] = df.loc[i, 'a_cybs']
    else:
        df.loc[i, 'cybs'] = df.loc[i, 'a_cybs'] - df.loc[i - 1, 'a_cybs']

df.to_csv('./takeoff.csv', index=False)

df.donors = df.donors.apply(lambda x: address_to_address(x, 'cyber'))
w_df = df[['donors', 'cybs']].copy()
w_df['cybs'] = w_df['cybs'] * 1_000_000_000
w_df = w_df.groupby(['donors']).sum()
w_df = w_df.round(0)
w_df.cybs = w_df.cybs.astype(int)
w_df = w_df.reset_index()

w_df.to_csv('./takeoff_leaderboard.csv', index=False)
