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


def get_validators_distributions(distribution_json):
    return [
        AbsoluteCSVProcessor(
            expected_emission=distribution_json["validators_drop"],
            distribution_type="validators_drop",
            path=VALIDATORS_PATH_CSV
        )
    ]

def get_urbit_distributions(distribution_json):
    return [
        AbsoluteCSVProcessor(
            expected_emission=distribution_json["urbit_drop"],
            distribution_type="urbit_drop",
            path=URBIT_PATH_CSV
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
                + get_validators_distributions(distribution_json) \
                + get_urbit_distributions(distribution_json) \
                + get_relative_distributions(distribution_json)

    return [processor.process() for processor in processors]


def concatenate_balances(all_balances):
    balances_df = pd.concat(all_balances, sort=False)
    # balances_df["number"] = range(balances_df.shape[0])
    balances_df = balances_df.groupby("address", sort=False).agg({
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

    genesis_json["app_state"]["auth"]["accounts"] = [{
        "type": "cosmos-sdk/Account",
        "value": {
            "address": address,
            "coins": [
                {
                    "denom":  DENOM,
                    "amount": str(row["cyb_balance"])
                }
            ],
            "public_key": "",
            "account_number": str(row["number"]),
            "sequence": "0"
        }
    } for address, row in balances.sort_values("number").iterrows()]

    genesis_json["app_state"]["distribution"]["fee_pool"]["community_pool"] = [{
            "denom": DENOM,
            "amount": distribution_json['community_pool']
    }]

    genesis_json["app_state"]["pool"] = {
            "not_bonded_tokens": distribution_json["total"],
            "bonded_tokens": "0"
    }

    genesis_json["app_state"]["supply"]["supply"] = [{
            "denom": DENOM,
            "amount": distribution_json['total']
    }]

    sum_amt_accs = sum([int(i["value"]['coins'][0]['amount']) for i in genesis_json["app_state"]["auth"]["accounts"]])
    print(DENOM, 'sum of accounts:', sum_amt_accs)

    community_pool = int(genesis_json["app_state"]["distribution"]['fee_pool']['community_pool'][0]["amount"])
    print(DENOM, 'in community pool:', community_pool)

    summ = sum_amt_accs + community_pool
    delta = int(genesis_json["app_state"]["supply"]["supply"][0]["amount"]) - summ

    print("sum accounts and cummunity pool:", summ, "expected:", genesis_json["app_state"]["supply"]["supply"][0]["amount"], "delta:", delta, DENOM)
    print("Allocate change dust to cummunity pool and save to .json")

    community_pool += delta

    genesis_json["app_state"]["distribution"]["fee_pool"]["community_pool"] = [{
            "denom": DENOM,
            "amount": str(community_pool)
    }]


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
