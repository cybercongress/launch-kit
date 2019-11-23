import json
import os

print("loading json...")

with open('data/genesis.json', 'r') as f:
    genesis_dict = json.load(f)

print("genesis.json loaded")

path = "data/gen_txs/"
gentxslist = os.listdir(path)
gentxs = []

for file in gentxslist:
    file = path + file
    with open(file, 'r') as f:
        gentxs.append(json.load(f))

print("gen_tx files loaded")

genesis_dict["app_state"]["gentxs"] = gentxs

print("gentxs added")

print("saving to signed_genesis.json")

with open('data/signed_genesis.json', 'w') as fp:
    json.dump(genesis_dict, fp)

print("done")