# Cosmos gift tool

The tool for collecting Cosmos network addresses with balances to future gifts. It's kinda preparation tool the output is .csv file with addresses and balances on the current snapshot.

## Requirements
 - [gaia ](https://github.com/cosmos/gaia/blob/master/docs/installation.md)
 - [cosmoshub-2 network](https://github.com/cosmos/gaia/blob/master/docs/join-mainnet.md) synced at least `1110001` block
 - [python3](https://realpython.com/installing-python/)
 - [launch-kit repo](https://github.com/cybercongress/launch-kit)
 - [pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)

 ## Preparations

 1. Make sure you cosmoshub-2 node have synced t least 1110001 block. For boosting the sync process you can follow [this guide](https://docs.chainlayer.io/quicksync/cosmos-snapshot). 
 2. You cannot export the state while having the node run. Temporarily halt the node and then perform an export
 3. Run the following command: 
 ```bash
 gaiad export --for-zero-height --height=1110000 --home=<PATH_TO_GAIA_HOME_DIRECTORY> > cosmos_genesis_snapshot.json
 ```
 4. You should get the `cosmos_genesis_snapshot.json` file at the current directory
 5. Install `pandas` 
 ```bash
 pip3 install pandas
 ```

 ## Gifting

 6. Move `cosmos_genesis_snapshot.json` to `$PATH_TO_LAUNCH_KIT/launch-kit/cosmos_gift_tool/data`
 7. Run:
 ```bash
 python3 cosmos_gift_snapshot.py
 ```
 8. The `cosmos.csv` file will show up in 5-10 seconds at `$PATH_TO_LAUNCH_KIT/launch-kit/cosmos_gift_tool/data/cosmos.csv`

 Nice! Now you have all cosmos addresses with non-zero balances on type `cosmosaddress,cosmosbalance` in the .csv file. Now you need `cyber address converter` to convert `cosmos` addresses into `cyber`. More details in `cyber address converter` [README](../cyber_address_converter/README.md)