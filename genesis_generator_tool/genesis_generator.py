import json
from config import *
from processors.processors import (
    JSONProcessor, 
    RelativeCSVProcessor, 
    AbsoluteCSVProcessor, 
    check_balances
)
import pandas as pd


def load_config():
    distribution_json = json.load(open(DISTRIBUTION_PATH))
    manual_json = json.load(open(MANUAL_DISTRIBUTION_PATH))
    genesis_json = json.load(open(GENESIS_EXAMPLE_PATH))
    return distribution_json, manual_json, genesis_json


def get_json_distributions(distribution_json, manual_json):
    return [
        JSONProcessor(
            total_json=manual_json,
            expected_emission=distribution_json[distribution_type],
            distribution_type=distribution_type
        ) 
        for distribution_type in manual_json
    ]


def get_absolute_distributions(distribution_json):
    return [
        AbsoluteCSVProcessor(
            expected_emission=distribution_json["validators_drop"],
            distribution_type="validators_drop",
            path=VALIDATORS_PATH_CSV
        )
    ]


def get_relative_distributions(distribution_json):
    return [
        RelativeCSVProcessor(
            path=CSV_DISTRIBUTIONS[distribution_type],
            expected_emission=distribution_json[distribution_type],
            emission=distribution_json[distribution_type],
            distribution_type=distribution_type
        )
        for distribution_type in CSV_DISTRIBUTIONS
    ]


def get_distributions(distribution_json, manual_json):
    processors = get_json_distributions(distribution_json, manual_json) \
                + get_absolute_distributions(distribution_json) \
                + get_relative_distributions(distribution_json)

    return [processor.process() for processor in processors]


def concatenate_balances(all_balances):
    balances_df = pd.concat(all_balances, sort=False)
    # balances_df["number"] = range(balances_df.shape[0])
    # balances_df["number"] += 1
    balances_df = balances_df.groupby("address").agg({
        "cyb_balance": "sum",
        # "number": "min"
    })
    balances_df["number"] = range(balances_df.shape[0])
    balances_df["cyb_balance"] = balances_df["cyb_balance"].astype(int)
    return balances_df


def save_json(distribution_json, genesis_json, balances):
    (
        balances["cyb_balance"],
        float(distribution_json["total"]), 
        "total"
    )
    genesis_json["app_state"]["accounts"] = [{
        "address": address,
        "coins": [
            {
                "denom":  "eul",
                "amount": str(row["cyb_balance"])
            }
        ],
        "sequence_number": "0",
        "account_number": str(row["number"]),
        "original_vesting": [],
        "delegated_free": [],
        "delegated_vesting": [],
        "start_time": "0",
        "end_time": "0",
        "module_name": "",
        # "module_permissions": "null"
    } for address, row in balances.sort_values("number").iterrows()]

    json.dump(
        genesis_json,
        open(GENERATED_GENESIS_PATH, "w")
    )


def generate():
    distribution_json, manual_json, genesis_json = load_config()
    all_balances = get_distributions(distribution_json, manual_json)
    cyb_balances_df = concatenate_balances(all_balances)
    save_json(distribution_json, genesis_json, cyb_balances_df)


if (__name__ == "__main__"):
    generate()
