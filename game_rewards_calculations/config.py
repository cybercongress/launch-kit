from string import Template
from progressbar import Bar, ETA, FileTransferSpeed, Percentage, ProgressBar

# put the block number (int) less or equal you need to calculate precommits in HEIGHT variable
# put the graphql API endpoint (str) in GRAPHQL_API variable
# fill the HEADERS dictionary accordingly graphql engine permissions

# HEIGHT = int
# GRAPHQL_API = str
# HEADERS = {
#     'content-type': 'application/json',
#     "authorization": ''
#   }

# the GRAPQL query for all validators consensus pub keys getting
VALIDATORS_Q = '''{
      validator(distinct_on: consensus_pubkey) {
        consensus_pubkey
      }
    }'''

# the GRAPQL query for getting all precommits on less or equal HEIGHT on validator consensus pub key
PRECOMMITS_Q = Template('''{
  pre_commit_aggregate(where: {
    _and:[
      {validator: {consensus_pubkey: {_eq: $addr}}},
      {height: {_lte: $height}}
    ]
  } ) {
    aggregate {
      count
    }
  }
}''')

# the progress bar variables
WIDGETS = ['Test: ', Percentage(), ' ',
               Bar(marker='-',left='[',right=']'),
               ' ', ETA(), ' ', FileTransferSpeed()]
PBAR = ProgressBar(widgets=WIDGETS, maxval=500)