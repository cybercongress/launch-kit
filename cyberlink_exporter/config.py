from string import Template
from progressbar import Bar, ETA, FileTransferSpeed, Percentage, ProgressBar

# put the block number (int) less or equal you need to calculate precommits in HEIGHT variable
# put the graphql API endpoint (str) in GRAPHQL_API variable
# fill the HEADERS dictionary accordingly graphql engine permissions

# HEIGHT = 
# GRAPHQL_API = ''
# HEADERS = {
#     'content-type': 'application/json',
#     "authorization": ''
#   }

# the GRAPQL query for getting all cyberlinks on less or equal block HEIGHT
CYBERLINKS_Q = Template('''{
  cyberlink(where: {block: {height: {_lte: $height}}}) {
    subject
    object_from
    object_to
  }
}''')

# the progress bar variables
WIDGETS = ['Test: ', Percentage(), ' ',
               Bar(marker='-',left='[',right=']'),
               ' ', ETA(), ' ', FileTransferSpeed()]
PBAR = ProgressBar(widgets=WIDGETS, maxval=500)