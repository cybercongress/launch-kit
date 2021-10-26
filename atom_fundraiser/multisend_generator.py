import pandas as pd
import json

data = pd.read_csv("./data/sendout.csv", header=None)
data = data.rename(columns = {0: "address", 1: "bounty"})

data = data.groupby(['address']).sum().reset_index()

print(data.shape[0])
print(data.bounty.sum())


sender = 'cosmos1e859xaue4k2jzqw20cv6l7p3tmc378pc5znax0'

msgs = []

for index, row in data.iterrows():
    msg = {
        "type": "cosmos-sdk/MsgSend",
        "value": {
            "from_address": sender,
            "to_address": row['address'],
            "amount": [
                {
                    "denom": "uatom",
                    "amount": str(int(row['bounty']))
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
            "gas": "2000000"
        },
        "signatures": None,
        "memo": "Refund of shares for slashing on block 4629079"
    }
}

with open("./data/unsigned.json", "w") as fp:
    json.dump(tx,fp, indent=4)