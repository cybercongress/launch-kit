from google.cloud import bigquery
import pandas as pd
from tqdm import tqdm
import click
from config import *


bigquery_balances_sql = """
with balances_table as (
    with double_entry_book as (
        -- debits
        select to_address as address, value as value, 0 as out_transaction
        from `bigquery-public-data.ethereum_blockchain.traces`
        where to_address is not null
        and block_number <= {block_number}
        and status = 1
        and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
        union all
        -- credits
        select from_address as address, -value as value, 1 as out_transaction
        from `bigquery-public-data.ethereum_blockchain.traces`
        where from_address is not null
        and block_number <= {block_number}
        and status = 1
        and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
        union all
        -- transaction fees debits
        select miner as address, sum(cast(receipt_gas_used as numeric) * cast(gas_price as numeric)) as value, 0 as out_transaction
        from `bigquery-public-data.ethereum_blockchain.transactions` as transactions
        join `bigquery-public-data.ethereum_blockchain.blocks` as blocks on blocks.number = transactions.block_number
        where block_number <= {block_number}
        group by blocks.miner
        union all
        -- transaction fees credits
        select from_address as address, -(cast(receipt_gas_used as numeric) * cast(gas_price as numeric)) as value, 0 as out_transaction
        from `bigquery-public-data.ethereum_blockchain.transactions`
        where block_number <= {block_number}
    )
    select address, sum(value) as balance, sum(out_transaction) as out_transactions
    from double_entry_book
    group by address
)
select address, balance, out_transactions
from balances_table
where balance > 0
and address not in (select address from `bigquery-public-data.ethereum_blockchain.contracts`)
order by balance desc
"""


def extract_balances(block_number):
    client = bigquery.Client.from_service_account_json(
        GOOGLE_KEY_PATH
    )
    sql = bigquery_balances_sql.format(block_number=block_number)
    query = client.query(sql)
    result = query.result()
    balances = [dict(row) for row in tqdm(result, total=result.total_rows)]
    return balances


def create_dataframe(balances):
    balances_df = pd.DataFrame(balances)
    balances_df["balance"] = (balances_df["balance"] / (10 ** 18)).astype(float)
    return balances_df


def cut_balances(balances_df):
    sum_threshold = balances_df["balance"].sum() * ETHEREUM_THRESHOLD
    balances_sum = balances_df["balance"].cumsum()
    balances_df = balances_df[(balances_sum <= sum_threshold) & (balances_df["out_transactions"] > 0)]
    return balances_df


def save_balances(balances_df):
    balances_df.drop(columns=["out_transactions"]).set_index("address").to_csv(ETHEREUM_GENESIS_PATH_CSV, header=False)


@click.command()
@click.option('--block', default=DEFAULT_ETHEREUM_BLOCK, help='Last block of ethereum state for genesis')
def extract(block):
    balances = extract_balances(block)
    balances_df = create_dataframe(balances)
    balances_df = cut_balances(balances_df)
    save_balances(balances_df)


if (__name__ == "__main__"):
    extract()
