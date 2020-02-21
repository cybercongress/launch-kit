# Genesis ceremony

If you in the list of Genesis validators you will get automatically respect from the community. It's a law.

This ceremony provides to validators sign the first transaction and start validating from the first block.

## Requirements

- [go1.13+](https://tecadmin.net/install-go-on-ubuntu/)
- [ipfs](https://docs.ipfs.io/guides/guides/install/)
- [cyberd and cyberdcli](https://github.com/cybercongress/cyberd)
- keys

## Flow

The flow is pretty simple:

1. Clone `cyberd` repo

```bash
git clone https://github.com/cybercongress/cyberd.git
```

2. Usually, you just need to switch the branch according to the network ID but if you confused just ask the correct version in telegram [chat](https://t.me/fuckgoogle)

3. Go inside repo:

```bash
cd cyberd
```

and run:

```bash
make
```

> if you get this message `Makefile:42: *** CUDA not installed for GPU support, please install or set CUDA_ENABLED=false.  Stop.` use `nano makefile` and change `CUDA_ENABLED=false`

to install `cyberd` and `cyberdcli` globally, and execute them by `cyberd` and `cyberdcli` commands, or run:

```bash
go build -o cyberd ./cmd/cyberd
go build -o cyberdcli ./cmd/cyberdcli
```

to install locally and execute them by `./cyberd` and `./cyberdcli` commands inside the repo.

4. Create directory for `cyberd` and `cyberdcli` data:

```bash
mkdir cyberdata
cd cyberdata
mkdir cyberd
mkdir cyberdcli
```

5. Initialize cyberd repo:

```bash
cyberd init --home <PATH_TO_CYBERD>/cyberdata/cyberd
```

6. Put your:

- `node_key.json`
- `priv_validator.json`

to `<PATH_TO_CYBERD>/cyberdata/cyberd/config` (overwrite existed)
and

- `keys.db`

to `<PATH_TO_CYBERD>/cyberdata/cyberdcli/keys`

7. Check your validator consensus pubkey and you cyber address by following comands:

```bash
cyberd tendermint show-validator --home <PATH_TO_CYBERD>/cyberdata/cyberd
cyberdcli keys list --home <PATH_TO_CYBERD>/cyberdata/cyberdcli
```

if all your necessary keys exists you can sign genesis file

8. go to `cyberdata/cyberd` directory, remove existing `genesis.json` and get the genesis.json by the following command:

```bash
ipfs get <GENESIS_HASH> -o genesis.json
```

The `genesis.json` file huge, so it can get a time.

9. Sign it. The transaction structure pretty similar for validator creation transaction:

```bash
cyberd gentx \
    --amount eul     \
    --commission-max-change-rate  \
    --commission-max-rate  \
    --commission-rate  \
    --home-client <PATH_TO_CYBERD>/cyberdata/cyberdcli \
    --min-self-delegation "" \
    --name <key_name>      \
    --node-id <nod_moniker> \
    --output-document <validator_moniker>.json \
    --pubkey <validator_consensus_pubkey> \
    --home <PATH_TO_CYBERD>/cyberdata/cyberd
```

The output file is signed genesis transaction for validator creation

10. Fork this repo 

```
https://github.com/cybercongress/launch-kit.git
```

11. Clone it, put your transaction file to `gen_txs/data/gen_txs/`, and submit PR. 

12. Done! 