# Genesis ceremony

Validators who get to participate in the Genesis block are more likely to get more respect from the community. It's the law.

To achieve this, we have a Genesis ceremony. This ceremony provides validators with the ability to sign the first transaction and start validating from the first block.

## Requirements

- [ipfs](https://docs.ipfs.io/guides/guides/install/)
- [cyberd and cyberdcli](https://github.com/cybercongress/go-cyber)

## Flow

The flow is pretty simple:

1. Install `cyberd` and `cyberdcli` on your computer use by the following command:

```bash
sudo bash < <(curl -s https://mars.cybernode.ai/go-cyber/install_cyberdcli_v0.1.6.sh)
```

2. Import your account to cyberdcli that you want to launch a validator from. Make sure you import an account with a non-zero balance. You can check the balance using [cyber.page gift tool](https://cyber.page/) by entering your validator address (if you had a gift for `euler-4` validating), or `Cosmos` and `Ethereum` addresses.

If you are importing a `cosmos` address or a previous validator address (that has already validated cyber on previous `euler` testnets), use the following command:

```bash
cyberdcli keys add <your_account_name> --recover
```

(<your_account_name> is the desired name for your account. Don't forget to remove the `<` and the `>` symbols)

and then input your bip39 mnemonic

If you are importing an address that had a `Urbit` or an `Ethereum` gift, then:

```bash
cyberdcli keys add private <your_account_name>
```

and then input your HEX private key.

The keys will be stored at your `$HOME/.cyberdcli/keys` directory, locally on your machine. Please make sure your machine is safe to keep your keys on it.

Awesome! You now have the keys for making the first transaction. 

3. Prepare a directory for `cyberd` data:

```bash
mkdir $PATH_TO_CYBERD/.cyberd
```

4. Initialize cyberd repo:

```bash
cyberd init <your_validator_moniker> --home $PATH_TO_CYBERD/.cyberd
```

If you will not add the `--home` flag, the initiation of `.cyberd` will happen in your `$HOME/.cyberd` directory. 

5. Get the `genesis.json` file from the IPFS hash:

```bash
ipfs get Qm... -o $PATH_TO_CYBERD/.cyberd/config/genesis.json
```

The `genesis.json` file is huge. It can take time do download it.

7. Check your validator consensus pubkey and you cyber address with the following commands:

```bash
cyberd tendermint show-validator --home $PATH_TO_CYBERD/.cyberd
cyberdcli keys list
```

> **IMPORTANT**
You need to backup your `$PATH_TO_CYBERD/.cyberd/config/node_key.json` and `$PATH_TO_CYBERD/.cyberd/config/priv_validator_key.json` files and import them onto your production node before the launch of the network! If you will lose these files, your node won't sing blocks. 

If all your necessary keys exist you can sign the genesis file.

8. Sign it. The transaction structure is pretty similar to the creation of a validator launching:

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

The output file is the signed genesis transaction for validator creation. It is located at `$PATH_TO_CYBERD/.cyberd`

9. Fork this repo 

```bash
https://github.com/cybercongress/launch-kit.git
```

10. Clone it, put your transaction file to `gen_txs/data/gen_txs/`, and submit PR. 

11. Done! 
