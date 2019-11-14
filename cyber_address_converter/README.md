# Cosmos Address Tool
The tool for converting `ethereum` and `cosmos addresses` into `cyber`.

## Requirements

- [go1.12+](https://golang.org/doc/install)

## Preparation

1. You need to build tool. Run

```bash
go build -o cyber ./
```
If it go tight you can see after build binary tool `cyber` in the current repo

## Cosmos to Cyber

For converting `cosmos` addresses into `cyber` copy prepared previously `cosmos.csv` file from `../cosmos_gift_tool/data/cosmos.csv` to the current repo

```bash
cp ../cosmos_gift_tool/data/cosmos.csv cosmos.csv
```

run:

```bash
./cyber convert-cosmos-batch cosmos.csv ./cosmos.csv --acc-prefix=cyber
```
It should take 2 minutes. The new `cosmos.csv` file will replace the old one in the current repo. The data structure is now `cyberaddress, cosmosbalances`

## Ethereum to cyber

For converting `ethereum` addresses into `cyber` copy prepared previously `ethereum.csv` file from `../ethereum_gift_tool/data/ethereum.csv` to the current repo

```bash
cp ../ethereum_gift_tool/data/ethereum.csv ethereum.csv
```

Also, you need `ethereum` public keys for converting. If you have alredy synced `parity` node synced at least `8080808` block you can just copy `eth-pubkeys` to the current directory. Otherwise you need to collect them. Run:

```bash
./cyber collect-ethereum-keys --node-url=http://localhost:8546 --threads=10
```
This script connects to a web3 client and pulls transaction data from the blockchain. In particular, it extracts r,v,s signature components of each transaction and calculates the secp256k1 public key associated with the Ethereum account that created the transaction. Collected data are stored in LevelDb as current sub-folder "eth-pubkeys".

Then you're redy for converting. Run:

```bash
./cyber convert-ethereum-batch ethereum.csv eth-pubkeys --acc-prefix=cyber
```

The process should take 2 minutes. The new `ethereum.csv` file will replace the old one in the current repo. The data structure is now `cyberaddress, ethereumbalances`

## Cybervaloper to Cyber

This tool convert validator rewards file from `cybervaloper address` into `cyber.`

Copy prepared previously `validators.csv` file from `../lifetime_rewards_tool/data/notebool/validators.csv` to the current repo

```bash
cp ../lifetime_rewards_tool/data/notebool/validators.csv validators.csv
```

run:

```bash
./cyber convert-cosmos-batch validators.csv ./validators.csv --acc-prefix=cyber
```
It should take few seconds. The new `validators.csv` file will replace the old one in the current repo. The data structure is now `cyberaddress, cyberbalance`
