import json
import pandas as pd
from config import *


def get_accounts():
    genesis_json = json.load(open(COSMOS_GENESIS_PATH))
    accounts = genesis_json["app_state"]["accounts"]
    accounts_prepared = [{
            "address": account["address"],
            "balance": int(account["coins"][0]["amount"])
        }
        for account in accounts
        if account["coins"]
    ]
    return accounts_prepared


def create_genesis(accounts):
    genesis_df = pd.DataFrame(accounts).set_index("address")
    return genesis_df


def save_genesis(genesis_df):
    genesis_df.to_csv(COSMOS_GENESIS_PATH_CSV, header=False)


def extract():
    accounts = get_accounts()
    genesis_df = create_genesis(accounts)
    save_genesis(genesis_df)

if (__name__ == "__main__"):
    extract()