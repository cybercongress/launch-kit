from celery import Celery
import requests
import json
import subprocess
import os
from tqdm import tqdm
import pandas as pd
from config import *
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
import logging
import pprint


app = Celery('scraper', broker='redis://')

def get_collection():
    client = MongoClient()
    database = client[DATABASE]
    collection = database["validators"]
    return collection

def print_progress():
    start_blocks = get_start_blocks()
    logging.warning("Current progress: {}".format(start_blocks))

def get_start_blocks():
    collection = get_collection()
    aggregation = collection.aggregate([{         
        "$group" : {            
            "_id": {"$mod": ["$block", THREADS]},            
            "block": {"$max": "$block"}      
        }       
    }])
    return dict([(pair["_id"], pair["block"]) for pair in aggregation])

def parse(json_response):
    block_json = json_response["result"]["block"]
    item = {
        "block": int(block_json["header"]["height"]),
        "validators": [commit["validator_address"] for commit in block_json["last_commit"]["precommits"] if commit],
        # Uncomment next line if you need full block info
        # "summary": json.dumps(json_response)
    }
    item["_id"] = item["block"]
    return item

def write(blocks):
    collection = get_collection()
    if not blocks:
        return
    try:
        collection.insert_many(blocks, ordered=False)
    except BulkWriteError as ex:
        logging.info(ex.details)

@app.task
def scrape(start_block, thread):
    logging.warning("Started thread {} from block {}".format(thread, start_block))
    blocks = []
    for block_index in range(start_block, start_block + CHUNK_SIZE):
        if block_index % THREADS != thread:
            continue
        try:
            url = "http://{}:{}/block?height={}".format(NODE_HOST, NODE_PORT, block_index)
            response = requests.get(url).json()
            if "error" in response:
                raise requests.exceptions.ConnectionError()
            block = parse(response)
            blocks.append(block)
        except requests.exceptions.ConnectionError:
            logging.error("Error while parsing {} block in thread {}, retrying".format(
                block_index, 
                thread
            ))
            block_index -= 1
            break

    block_index += 1
    write(blocks)
    scrape.delay(block_index, thread)
    print_progress()

if __name__ == "__main__":
    start_blocks = get_start_blocks()
    for thread in range(THREADS):
        start_block = start_blocks.get(thread, FIRST_BLOCK)
        print("{} thread starts from block {}".format(thread, start_block))
        scrape.delay(start_block, thread)