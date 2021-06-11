import pandas as pd
import requests


from config import CYBER_LCD

PROXY_ADDRESS = 'cyber1uvqp7cqzpzjxwxlx87epgf8er9az89f9jpzcyh'
PROXY_ADDRESS_2 = 'cyber1mlqakhlxplhlezk80lph99wcy377j9dkwc42l4'


def get_addresses():
    resp = requests.get(CYBER_LCD + '/gov/proposals?status=passed').json()
    df = pd.DataFrame(columns=['subject', 'reward', 'description'])
    for res in resp['result']:
        if res['content']['type'] == 'cosmos-sdk/CommunityPoolSpendProposal':
            subject = res['content']['value']['recipient']
            reward = int(res['content']['value']['amount'][0]['amount'])
            title = res['content']['value']['title']
            df = df.append({
                'subject': subject,
                'reward': reward,
                'description': title
            }, ignore_index=True)
        else:
            pass
    return df


def get_from_proxy_addresses(proxy_address):
    proxy_resp = requests.get(CYBER_LCD + f'/txs?message.action=send&message.sender={proxy_address}&limit=1000').json()
    __df = pd.DataFrame(columns=['subject', 'reward', 'description'])
    for tx in proxy_resp['txs']:
        _df = pd.DataFrame(columns=['subject', 'reward', 'description'])
        memo = tx['tx']['value']['memo']
        for message in tx['tx']['value']['msg']:
            subject = message['value']['to_address']
            reward = int(message['value']['amount'][0]['amount'])
            _df = _df.append({
                'subject': subject,
                'reward': reward,
                'description': memo
            }, ignore_index=True)
        __df = __df.append(_df, ignore_index=True)
    comm_pool = __df.reward.sum()
    return __df, comm_pool


def get_from_proxy_addresses2(proxy_address):
    proxy_resp = requests.get(CYBER_LCD + f'/txs/D0C6305F33994B6767C37DCB1D6EDD756933D8358F2A69FF717BC59784659835').json()
    __df = pd.DataFrame(columns=['subject', 'reward', 'description'])
    for message in proxy_resp['tx']['value']['msg']:
        subject = message['value']['to_address']
        reward = int(message['value']['amount'][0]['amount'])
        __df = __df.append({
            'subject': subject,
            'reward': reward,
            'description': 'video bounty'
        }, ignore_index=True)
    comm_pool = __df.reward.sum()
    return __df, comm_pool


def get_cp_rewards():
    proposals = get_addresses()
    sergey, sergey_sum = get_from_proxy_addresses(PROXY_ADDRESS)
    vladimir, vladimir_sum = get_from_proxy_addresses2(PROXY_ADDRESS_2)
    df = pd.concat([proposals, sergey, vladimir])
    df = df.drop(['description'], axis=1)
    df = df.groupby(['subject']).sum()
    df = df.drop(PROXY_ADDRESS)
    df.loc[PROXY_ADDRESS_2]['reward'] -= vladimir_sum
    df = df.reset_index()
    df = df.sort_values(by=['reward'], ascending=False)
    df.to_csv('./data/comm_pool_rewards.csv')
