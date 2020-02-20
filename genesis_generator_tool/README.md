# Genesis generator tool

This tool provides `genesis.json` file compilation from the next following files: 

- `network_genesis.json`
- `cyber_distribution.json`
- `manual_distribution.json`
- `ethereum.csv`
- `cosmos.csv`
- `urbit.csv`
- `validators.csv`

As output of this script is generated `genesis.json` file ready for signing. All files above should be at `./data` folder, the `genesis.json` is saving in the same folder.

The `network_genesis.json` should contain all network parameters including network launch time and excluding accounts.

The `cyber_distribution.json` should contain account groups and token balances by each group. The sum of group balances should be equal to the total supply of genesis distribution.

The `manual_distribution.json` should contain special addresses divided by groups existed in `cyber_distribution.json`. These is all non-gift addresses.

The `ethereum.csv` is the file with ethereum balances but with converted to `cyber` addresses like:

```bash
cyber_address, ethereum_balance
```

The `cosmos.csv` is the file with cosmos balances but with converted to `cyber` addresses like:

```bash
cyber_address, cosmos_balance
```

The `urbit.csv` file contains converted to `cyber` ethereum accounts with Urbit entities. The balances in `cyber` network should be calculated before. See the [urbit_gift_tool](../urbit_gift_tool/README.md) folder. 

The `validators.csv` file contains converted to `cyber` `cybervaloper` accounts with `euler-4` validators. The balances in `cyber` network should be calculated before. See the [lifetime_rewards_tool](../lifetime_rewards_tool/README.md) folder. 

If the `./data` folder contains necessary files the genesis generator tool should work correctly.

1. The script loads all files from `./data` folder
2. Calculate gifts for `ethereum` and `cosmos` accounts by quadratic distribution
3. Get all accounts and group them by addresses with the account sum. 
4. Check sum of all accounts balances with total supply, if the change less than `0.0001` the script allocates it to the community pool. This is a normal thing like change or dust in that calculations because of the number of addresses and complex distribution functions.
5. Put addresses and balances to genesis structure to the correct format.
5. Save genesis structure to `genesis.json`