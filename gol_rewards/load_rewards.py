import requests
import pandas as pd
import asyncio
import aiohttp
import json
import time


from config import CYBER_LCD, TXS_LIMIT, TABLE, CHUNK, KARMA_BLOCK_HEIGHT, LOAD_REWARD
from utils.db import create_table, insert_to_db, is_table_exist, fix_karma, karma_grouped_to_df


def get_pages(height_range):
    try:
        res = requests.get(
            CYBER_LCD + f'/txs?message.action=link&page=1&limit={TXS_LIMIT}&tx.minheight={height_range[0]}&tx.maxheight={height_range[1]}').json()
        page_total = int(res['page_total'])
    except Exception as e:
        print(e)
        time.sleep(2)
        get_pages(height_range)
    print('--------------', page_total)
    return page_total


async def fetch(session, page, height_range):
    url = CYBER_LCD + f'/txs?message.action=link&page={page}&limit={TXS_LIMIT}&tx.minheight={height_range[0]}&tx.maxheight={height_range[1]}'
    try:
        async with session.get(url) as response:
            data = await response.read()
        txs = json.loads(data)['txs']
        for tx in txs:
            result = [(
                tx['timestamp'],
                int(tx['height']),
                tx['txhash'],
                log['events'][0]['attributes'][0]['value'],
                log['events'][0]['attributes'][1]['value'],
                log['events'][1]['attributes'][0]['value'],
                int(log['events'][1]['attributes'][1]['value'])
            ) for log in tx['logs']]
            insert_to_db(result, TABLE)
    except Exception:
        await asyncio.sleep(5)
        await fetch(session, page, height_range)



async def fetch_all(loop, pages, height_range):
    semaphore = asyncio.Semaphore(50)
    async with semaphore:
        async with aiohttp.ClientSession(loop=loop) as session:
            await asyncio.gather(*[fetch(session, page, height_range) for page in range(1, pages + 1)])


def pre_processor(height_range):
    pages = get_pages(height_range)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all(loop, pages, height_range))


def processor():
    ranges = [(n + 1, min(n + CHUNK, KARMA_BLOCK_HEIGHT)) for n in range(1, KARMA_BLOCK_HEIGHT, CHUNK)]
    for _range in ranges:
        print(_range)
        if is_table_exist(TABLE):
            pre_processor(_range)
        else:
            create_table(TABLE)
            pre_processor(_range)


def get_load_rewards():
    processor()
    fix_karma(TABLE)
    df = karma_grouped_to_df(TABLE)
    df['reward'] = (df['karma'] / sum(df['karma'])) * LOAD_REWARD
    df = df.drop(['karma'])
    df['reward'] = df['reward'].round(0)
    df.to_csv('./data/load.csv')