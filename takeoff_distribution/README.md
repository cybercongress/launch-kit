# Takeoff distribution tool

This tool will help to distribute tokens according to distribution rules.

At the current implementation, this tool collects all donors transactions during the takeoff round and also gets addresses from the evangelism referral program. 

As a result - two prepared for signing and broadcasting `.json` files.

0. Clone launch-kit repo and make sure that you have `python3` and `pip3`.

```bash
git clone https://github.com/cybercongress/launch-kit
cd launch-kit/takeoff_distribution
```

1. Install requirements

```bash
pip3 install requirements.txt 
```

2. Fill the `config.py` file with credentials:

```python
CONGRESS_COSMOS_ADDRESS = 'cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a'
CONGRESS_CYBER_ADDRESS = 'cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8'
URL = '<GAIA_LCD>' + 'txs?message.action=send&transfer.recipient={}&page={}'
takeoff_distr = 100000000000000 # 100 TEUL
from_date = '2020-03-30 00:00:00'
to_date = '2020-12-01 00:00:00'
ETH_NODE_RPC = '<ETH_NODE_RPC>'
```

Actually and gaia LCD url and ethereum node RPC.

3. Run

```bash
python3 main.py
```

It will take approximately 30-40 seconds. The output will like
```bash
99999999999992 EULs allocated, or: 99.999999999992 TEULs
1010280712 cashback uATOMs, or: 1010.280712 ATOMs
```
that summarized distribution.

The result you will see in the `data` folder. You may find `distribution.csv` table with all data collected from LCD and RPC according to the configured account. 

Also, you can find `cashback.csv`,  `takeoff.csv`, and `team.csv` tables grouped by addresses.

The final tables are `cyber.csv` and `cosmos.csv` - from those tables will be prepared transaction files. 

And, finally, `cyber.json` and `cosmos.json` - prepared for signing and broadcasting transactions in cyber and cosmos networks accordantly by `cyber` and `cosmos` multisigs accordantly.

4. After that, you need to make procedures of sign and broadcast `cyber.json` and `cosmos.json`.

[This article](https://cybercongress.ai/docs/go-cyber/multisig_guide/) should help you. You may start from `Spending out of a multisig account` section where `unsigned.json` is yours `cyber.json` and `cosmos.json` in correct networks.

Good luck!