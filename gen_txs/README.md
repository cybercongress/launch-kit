# Genesis ceremony

If you in the list of Genesis validators you will get automatically respect from the community.

This ceremony provides to validators sign the first transaction and start validating from the first block.

## Requirements

- [ipfs](https://docs.ipfs.io/guides/guides/install/)
- [cyberd and cyberdcli](https://github.com/cybercongress/go-cyber)

## Flow

The flow is pretty simple:

1. Install `cyberd` and `cyberdcli` on your computer use by the following command:

```bash
sudo bash < <(curl -s https://mars.cybernode.ai/go-cyber/install_cyberdcli_v0.1.6.sh)
```

2. Import to cyberdcli your account you want to launch a validator. Make sure you will import an account with non-zero balance: you can check it out with cyber.page gift tool by entering your validator address (if you have gift for `euler-4` validating), or `cosmos` and `ethereum` addresses.
Since v.38 cosmos-sdk uses os-native keyring to store all your keys. We've noticed that in several cases it does not work well by default (for example if you don't have GUI installed on your machine). If you face on with errors by executing commands below please check [this section](https://github.com/cybercongress/go-cyber/blob/0.1.6_run_out_of_docker/docs/run_validator.md#prepare-the-staking-address), or ask us at [telegram chat](https://t.me/fuckgoogle).
For `cosmos` and validator addresses use the following command, your account name is the whatever name you want for you :

```bash
cyberdcli keys add <your_account_name> --recover
```

and than input your bip39 mnemonic

for `urbit` and `ethereum`:

```bash
cyberdcli keys add private <your_account_name>
```

and than input you HEX private key

Nice. Now you hve a keys for making first transaction.

3. Prepare directory for `cyberd` data:

```bash
mkdir $PATH_TO_CYBERD/.cyberd
```

4. Initialize cyberd repo with validator moniker you want:

```bash
cyberd init <your_validator_moniker> --home $PATH_TO_CYBERD/.cyberd
```

If you will not add `--home` flag the `.cyberd` initiation will be at `$HOME/.cyberd` directory.

5. Get the `genesis.json` file by the IPFS hash:

```bash
ipfs get Qm... -o $PATH_TO_CYBERD/.cyberd/config/genesis.json
```

The `genesis.json` file huge, so it can get a time.

7. Check your validator consensus pubkey and you cyber address by following comands:

```bash
cyberd tendermint show-validator --home $PATH_TO_CYBERD/.cyberd
cyberdcli keys list
```

> **IMPORTANT**
You also need to backup your `$PATH_TO_CYBERD/.cyberd/config/node_key.json` and `$PATH_TO_CYBERD/.cyberd/config/priv_validator_key.json` files and import them to your production node before launch for correct working! If you will lose this files your node can't sign blocks. 

If all your necessary keys exists you can sign genesis file

8. Sign it. The transaction structure pretty similar for validator creation transaction:

```bash
cyberd gentx \
    --amount <>eul     \
    --commission-max-change-rate 0.01 \
    --commission-max-rate 0.1 \
    --commission-rate 0.03 \
    --min-self-delegation "10" \
    --name <key_name>      \
    --node-id <nod_moniker> \
    --output-document $PATH_TO_CYBERD/.cyberd/<validator_moniker>.json \
    --pubkey <validator_consensus_pubkey> \
    --home $PATH_TO_CYBERD/.cyberd
```

all params presented here just for example. You can import yours according to your validator strategy. 

The output file is signed genesis transaction for validator creation at `$PATH_TO_CYBERD/.cyberd`

9. Fork this repo

```bash
https://github.com/cybercongress/launch-kit.git
```

10. Clone it, put your transaction file to `gen_txs/data/gen_txs/`, and submit a PR. 

11. Done! 