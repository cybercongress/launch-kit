import requests
import json
import pandas as pd
from config import *

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(GRAPHQL_API, json={'query': query}, headers=HEADERS)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

print('Getting validators list')
validators = run_query(VALIDATORS_Q)['data']['validator']

vals = []

print('Calculating precommits for each validator')
for validator in PBAR(validators):
    val = json.dumps(validator['consensus_pubkey'])
    temp = [json.loads(val), run_query(PRECOMMITS_Q.substitute(addr = val, height = HEIGHT))['data']['pre_commit_aggregate']['aggregate']['count']]
    vals.append(temp)

print('Saving to /data/precommits.csv')
validators_df = pd.DataFrame(vals, columns=['address', 'precommits'])
validators_df.to_csv('./data/precommits.csv', index = None, header=None)
print('Done')