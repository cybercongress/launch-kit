# Ethereum gift tool

The tool for collecting Ethereum network addresses with balances to future gifts. It's kinda preparation tool the output is .csv file with addresses and balances on the current snapshot.

## Requirements
- [gcp project](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
- [python3](https://realpython.com/installing-python/)
- [pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)

## Preparations

1. Open `google-big-query-key.example.json` and fill sections with your gcp account credentials
2. Rename `google-big-query-key.example.json` to `google-big-query-key.json`
3. Check the `config.py` file. The `DEFAULT_ETHEREUM_BLOCK` variable should be  `8080808`, and `ETHEREUM_THRESHOLD` `0.997`. 
4. Install packages
 ```bash
 pip3 install pandas
 pip3 install google.cloud.bigquery
 pip3 install tqdm
 pip3 install click
 ```

## Gifting

3. Run:

```bash
python3 ethereum_gift_snapshot.py
```
The collecting process can take 30-40 minutes

4. The `ethereum.csv` file will show up at `$PATH_TO_LAUNCH_KIT/launch-kit/ethereum_gift_tool/data/ethereum.csv`

Nice! Now you have 80% ethereum addresses with non-zero balances, non-contracts and at least one outgoing transaction on type `ethereumaddress,ethereumbalance` in the .csv file. Now you need `cyber address converter` to convert `ethereum` addresses into `cyber`. More details in `cyber address converter` [README](../cyber_address_converter/README.md)