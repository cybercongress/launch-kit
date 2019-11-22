# Cosmos Address Tool
A tool for converting `ethereum` and `cosmos addresses` into `cyber`.

## Requirements

- [go1.12+](https://golang.org/doc/install)

## Preparation

1. You need to build the tool. 
Run:

```bash
go build -o cyber ./
```
If it goes right, you can see it after building the binary tool `cyber` in the current repo

## Cosmos to Cyber

For converting `cosmos` addresses into `cyber` copy the previously prepared `cosmos.csv` file from `../cosmos_gift_tool/data/cosmos.csv` to the current repo

```bash
cp ../cosmos_gift_tool/data/cosmos.csv cosmos.csv
```

run:

```bash
./cyber convert-cosmos-batch cosmos.csv ./cosmos.csv --acc-prefix=cyber
```
It should take 2 minutes. The new `cosmos.csv` file will replace the old one in the current repo. The data structure is now `cyberaddress, cosmosbalances`

## Ethereum to cyber

For converting `ethereum` addresses into `cyber` copy the previously prepared `ethereum.csv` file from `../ethereum_gift_tool/data/ethereum.csv` to the current repo

```bash
cp ../ethereum_gift_tool/data/ethereum.csv ethereum.csv
```

Also, you will need the `ethereum` public keys for converting. If you have alredy synced `parity` node (synced at least to `8080808` blocks), you can just copy `eth-pubkeys` to the current directory. Otherwise you need to collect them. 
Run:

```bash
./cyber collect-ethereum-keys --node-url=http://localhost:8546 --threads=10
```
This script connects to a web3 client and pulls transaction data from the blockchain. In particular, it extracts r,v,s signature components of each transaction, and calculates the secp256k1 public key associated with the Ethereum account that has created the transaction. The collected data is stored in LevelDb as current sub-folder "eth-pubkeys".

Then, you're redy for converting. 
Run:

```bash
./cyber convert-ethereum-batch ethereum.csv eth-pubkeys --acc-prefix=cyber
```

The process should take 2 minutes. The new `ethereum.csv` file will replace the old one in the current repo. The data structure is now `cyberaddress, ethereumbalances`

## Cybervaloper to Cyber

This tool converts the validator rewards file, from `cybervaloper address` into `cyber.`

Copy the previously prepared `validators.csv` file from `../lifetime_rewards_tool/data/notebool/validators.csv` to the current repo

```bash
cp ../lifetime_rewards_tool/data/notebool/validators.csv validators.csv
```

run:

```bash
./cyber convert-cosmos-batch validators.csv ./validators.csv --acc-prefix=cyber
```
It should take a few seconds. The new `validators.csv` file will replace the old one in the current repo. The data structure is now `cyberaddress, cyberbalance`
