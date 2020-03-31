# Genesis ceremony

If you in the list of Genesis validators you will get automatically respect from the community. It's a law.

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

2. Import your account to cyberdcli you want to launch a validator. Make sure you will import account with non-zero balance: you can check it out with cyber.page gift tool by entering your validator address (if you have gift for `euler-4` validating), or `cosmos` and `ethereum` addresses.

for `cosmos` and validator addresses use the following command:

```bash
cyberdcli keys add <your_account_name> --recover
```

and than input your bip39 mnemonic

for `urbit` and `ethereum`:

```bash
cyberdcli keys add private <your_account_name>
```

and than input you HEX private key

All keys will store at `$HOME/.cyberdcli/keys` directory.

Nice. Now you hve a keys for making first transaction. 

3. Prepare directory for `cyberd` data:

```bash
mkdir $PATH_TO_CYBERD/.cyberd
```

4. Initialize cyberd repo:

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
You also need to backup your `$PATH_TO_CYBERD/.cyberd/config/node_key.json` and `$PATH_TO_CYBERD/.cyberd/config/priv_validator_key.json` files and import them to your production node before launch for correct working! If you will lose this files your node can't sing blocks. 

if all your necessary keys exists you can sign genesis file

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

The output file is signed genesis transaction for validator creation at `$PATH_TO_CYBERD/.cyberd`

9. Fork this repo 

```bash
https://github.com/cybercongress/launch-kit.git
```

10. Clone it, put your transaction file to `gen_txs/data/gen_txs/`, and submit PR. 

11. Done! 