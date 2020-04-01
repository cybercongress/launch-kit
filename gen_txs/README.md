# Genesis ceremony
 
 Validators that participate in the Genesis block are more likely to get more respect from the community.
 
To achieve this, we have a Genesis ceremony. This ceremony provides validators with the ability to sign the first transaction and start validating from the very first block. 
 
 ## Requirements
 
 - [IPFS](https://docs.ipfs.io/guides/guides/install/)
 - [cyberd and cyberdcli](https://github.com/cybercongress/go-cyber)
 
 ## Flow
 
 The flow is pretty simple:
 
 1. Install `cyberd` and `cyberdcli` on your computer by using the following command:
 
 ```bash
 sudo bash < <(curl -s https://mars.cybernode.ai/go-cyber/install_cyberdcli_v0.1.6.sh)
 ```
 
 2. Import to cyberdcli the account you want to launch a validator from. Make sure that you import an account with a non-zero balance. You can check your balance on [cyber.page](cyber.page), using the gift tool by entering your validator address (if you had a gift for validating `euler-4`), or any `Cosmos` or `Ethereum` address that were eligible for a [gift](https://github.com/cybercongress/congress/blob/master/ecosystem/Gift%20FAQ%20and%20general%20gift%20information.md).
 
 Since cosmos-SDK v.38 uses an OS-native keyring to store all your keys, we've noticed that in some cases it does not work well by default (for example when you don't have any GUI installed on your machine). If you are facing errors when executing any of the commands below, please check [this section](https://github.com/cybercongress/go-cyber/blob/0.1.6_run_out_of_docker/docs/run_validator.md#prepare-the-staking-address) or give us a shout at our [telegram chat](https://t.me/fuckgoogle).
 
 If you are importing a `Cosmos` address or a previous validator address (that has already validated cyber on previous `euler` testnets), use the following command:
 
 ```bash
 cyberdcli keys add <your_account_name&gt; --recover
 ```
 
 (<your_account_name&gt; is the desired name for your account. Don't forget to remove the `<` and the `&gt;` symbols)
 
 and then input your bip39 mnemonic
 
 If you are importing an address that had an `Urbit` or an `Ethereum` gift, then:
 
 ```bash
 cyberdcli keys add private <your_account_name&gt;
 ```
 
 And then input your HEX private key (the system will ask you to add a password for encryption).
 
 The keys will be stored locally on your machine. Please make sure your machine is safe to keep your keys on it.
 
 Awesome! You now have the keys for making the first transaction. 
 
 3. Prepare a directory for `cyberd` data:
 
 ```bash
 mkdir $PATH_TO_CYBERD/.cyberd
 ```
 
 4. Initialize cyberd repo with a validator moniker that you want:
 
 ```bash
 cyberd init <your_validator_moniker&gt; --home $PATH_TO_CYBERD/.cyberd
 ```
 
&gt; **Important**

If you were a `euler-5` validator, please, copy your `node_key.json` and `priv_validator_key.json` from <PATH_TO_EULER-5_DATA>/cyberd/config and replace auto-generated files after the initialization.

 If you will not add the `--home` flag, the initiation of `.cyberd` will happen in your `$HOME/.cyberd` directory. 
 
 5. Get the `genesis.json` file from the IPFS hash:
 
 ```bash
 ipfs get QmYrZuyMvskb2tkY65Go1Dadh1axXjY4x3VfFadaSSRf8b -o $PATH_TO_CYBERD/.cyberd/config/genesis.json
 ```
 
 The `genesis.json` file is huge. It can take time do download it.
 
 7. Check your validator consensus pubkey and you cyber address with the following commands:
 
 ```bash
 cyberd tendermint show-validator --home $PATH_TO_CYBERD/.cyberd
 cyberdcli keys list
 ```
 
 &gt; **Important**
 You need to backup your `$PATH_TO_CYBERD/.cyberd/config/node_key.json` and `$PATH_TO_CYBERD/.cyberd/config/priv_validator_key.json` files and import them onto your production node before the launch of the network! If you will lose these files, your node won't sing blocks. 
 
 If all your necessary keys are in place, you are ready to sign the genesis file.
 
 8. Sign it. The transaction structure is pretty similar to the creation of a validator launching:
 
 ```bash
 cyberd gentx \
 --amount <&gt;eul \
 --commission-max-change-rate 0.01 \
 --commission-max-rate 0.1 \
 --commission-rate 0.03 \
 --min-self-delegation "10" \
 --name <key_name&gt; \
 --node-id <nod_moniker&gt; \
 --output-document $PATH_TO_CYBERD/.cyberd/<validator_moniker&gt;.json \
 --pubkey <validator_consensus_pubkey&gt; \
 --home $PATH_TO_CYBERD/.cyberd
 ```
 
 The params presented above are just an example. You may enter any params with accordance to your validator strategy. 
 
 The output file is the signed genesis transaction for validator creation. It is located at `$PATH_TO_CYBERD/.cyberd`
 
 9. Fork this repo
 
 ```bash
 https://github.com/cybercongress/launch-kit.git
 ```
 
 10. Clone it, put your transaction file to `gen_txs/data/gen_txs/`, and submit a [PR](https://github.com/cybercongress/launch-kit/pulls). 
 
 11. Done! 
