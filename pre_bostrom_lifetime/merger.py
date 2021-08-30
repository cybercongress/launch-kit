import pandas as pd
import requests
import base64
import bech32

url = 'https://lcd.bostromdev.cybernode.ai/cosmos/staking/v1beta1/validators'

df = df[['consensus_pubkey', 'consensus_address', 'precommits']]

validators = pd.read_csv('./pre_bostrom_lifetime/bostrom_testnet_1.csv')
precommits = pd.read_csv('./pre_bostrom_lifetime/bostrom_testnet_1_200k.csv')

res = requests.get(url).json()['validators']

def b64_to_cons(cons):
    cons = bytes(cons, 'utf-8')
    cons = base64.b64decode(cons)
    five_bit_r = bech32.convertbits(cons, 8, 5)
    return bech32.bech32_encode('bostromvalconspub', five_bit_r)

result = [(validator['operator_address'], b64_to_cons(validator['consensus_pubkey']['key']), validator['description']['moniker']) for validator in res]