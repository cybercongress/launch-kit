# Takeoff distribution tool

This tool can help to distribute tokens according to your own distribution rules.

The current implementation, collects all the transactions of the donors during the takeoff round (your auction) and collects addresses from the evangelism referral program (your ambassador programm).

As a result, the 2 are prepared for signing and broadcasting as `.json` files.

## Flow:

0. Clone the launch-kit repo and make sure that you have `python3` and `pip3` installed:

```bash
git clone https://github.com/cybercongress/launch-kit
cd launch-kit/takeoff_distribution
```

1. Install requirements:

```bash
pip3 install requirements.txt
```

2. Fill the `config.py` file with the following credentials:

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

3. Run:

```bash
python3 main.py
```

It will take approximately 30-40 seconds. The output will be:

```bash
99999999999992 EULs allocated, or: 99.999999999992 TEULs
1010280712 cashback uATOMs, or: 1010.280712 ATOMs
```

That summarizes the distribution.

You will see the results in the `data` folder. You may find the `distribution.csv` table with all the collected data from LCD and RPC points according to the configured account.

You will find the `cashback.csv`,  `takeoff.csv`, and `team.csv` tables grouped by addresses.

The final tables are `cyber.csv` and `cosmos.csv`. Out of these tables, you will be preparing the transaction files.

Finally, `cyber.json` and `cosmos.json` are prepared for signing and broadcasting transactions to Cyber and to the Cosmos network  with the help of `cyber` and `cosmos` multisigs.

4. After that you need to sign and broadcast `cyber.json` and `cosmos.json`.

[This article](https://cybercongress.ai/docs/go-cyber/multisig_guide/) should help you. You may start with the `Spending out of a multisig account` section, where `unsigned.json` is yours `cyber.json` and `cosmos.json` in the correct network.

Good luck!
