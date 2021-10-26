import pandas as pd
import json

with open('video_bounty.txt', 'r') as f:
     addresses = [line.strip() for line in f]

send = [50000000] * len(addresses)

data = {
    'address': addresses,
    'bounty': send
}

df = pd.DataFrame (data, columns = ['address', 'bounty'])

sender = 'cyber1mlqakhlxplhlezk80lph99wcy377j9dkwc42l4'

msgs = []

for index, row in df.iterrows():
    msg = {
        "type": "cosmos-sdk/MsgSend",
        "value": {
            "from_address": sender,
            "to_address": row['address'],
            "amount": [
                {
                    "denom": "eul",
                    "amount": str(row['bounty'])
                }
            ]
        }
    }
    msgs.append(msg)

tx = {
    "type": "cosmos-sdk/StdTx",
    "value": {
        "msg": msgs,
        "fee": {
            "amount": [],
            "gas": "200000"
        },
        "signatures": None,
        "memo": "by signing this transaction I agree with these payouts used as community pool tokens and the sum of payouts will be deducted from the current signing address in the mainnet as 1 to 1 EUL to CYB"
    }
}

with open("./data/unsigned.json", "w") as fp:
    json.dump(tx,fp, indent=4)