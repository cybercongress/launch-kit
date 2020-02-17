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

print('Getting all cyberlinks list')
cyberlinks = run_query(CYBERLINKS_Q.substitute(height = HEIGHT))['data']['cyberlink']

cyberlinks_df = pd.DataFrame(cyberlinks)
cyberlinks_df = cyberlinks_df.rename(columns={'object_from': 'from'})
cyberlinks_df = cyberlinks_df.rename(columns={'object_to': 'to'})
subjects = cyberlinks_df.subject.unique()

cyberlinks_ex = {}

for subject in PBAR(subjects):
    _cyberlinks_df_ = cyberlinks_df[cyberlinks_df.subject == subject][['from', 'to']]
    _cyberlinks = _cyberlinks_df_.to_dict('records')
    cyberlinks_ex[subject] =_cyberlinks

print('Saving to /data/cyberlinks.json')
with open('data/cyberlinks.json', 'w') as f:
    json.dump(cyberlinks_ex, f)
print('Done')