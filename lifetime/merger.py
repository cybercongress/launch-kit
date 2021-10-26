import pandas as pd
import requests
import base64
import bech32

from cyberpy._wallet import address_to_address

LCD_API = 'https://lcd.bostromdev.cybernode.ai'

url = LCD_API + '/cosmos/staking/v1beta1/validators'

res = requests.get(url).json()['validators']

def b64_to_cons(cons):
    cons = bytes(cons, 'utf-8')
    cons = base64.b64decode(cons)
    five_bit_r = bech32.convertbits(cons, 8, 5)
    return bech32.bech32_encode('bostromvalconspub', five_bit_r)

result = [(validator['operator_address'], b64_to_cons(validator['consensus_pubkey']['key']), validator['description']['moniker']) for validator in res]


pre_commits_bostrom_5 = pd.read_csv('./bostrom_testnet_5_360000.csv')
validators_bostrom_5 = pd.DataFrame(result, columns=['operator_address', 'consensus_pubkey', 'moniker'])
merged_df = validators_bostrom_5.merge(pre_commits_bostrom_5, how='outer', on=['consensus_pubkey'])
merged_df.dropna(subset=['precommits'], inplace=True)
merged_df = merged_df.reset_index(drop=True)
merged_df = merged_df[['moniker', 'operator_address', 'precommits']]

bostrom_1_4 = pd.read_csv('./result_4.csv')
bostrom_1_4 = bostrom_1_4[['moniker', 'operator_address', 'precommits']]

bostrom_1_4_monikers = bostrom_1_4[['moniker', 'operator_address']]
bostrom_5_monikers = merged_df[['moniker', 'operator_address']]
monikers = pd.concat([bostrom_1_4_monikers, bostrom_5_monikers]).drop_duplicates(
    subset=['operator_address'],
    keep='last').reset_index(drop=True)


result_precommits = pd.concat([merged_df, bostrom_1_4]).groupby(['operator_address']).sum().reset_index()
result_precommits = result_precommits.sort_values('precommits', ascending=False).reset_index(drop=True)

result_precommits = monikers.merge(result_precommits, how='outer', on=['operator_address'])
result_precommits = result_precommits.sort_values(by='precommits', ascending=False).reset_index(drop=True)

result_precommits = result_precommits[['moniker', 'operator_address', 'precommits']]

result_precommits['reward'] = (150_000_000_000/result_precommits['precommits'].sum() * result_precommits['precommits']).astype('int')

result_precommits.to_csv('result_5.csv')

bostrom_lifetime = result_precommits[['operator_address', 'reward']]

bostrom_lifetime['subject'] = bostrom_lifetime.apply(lambda x: address_to_address(x['operator_address'], 'bostrom'), axis=1)

bostrom_lifetime = bostrom_lifetime[['subject', 'reward']]

bostrom_lifetime.to_csv('./bostrom_lifetime.csv')

