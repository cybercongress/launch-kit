GRAPHQL_API = "https://port.cybernode.ai/graphql/v1/graphql"

HEADERS = {
    'content-type': 'application/json',
    "authorization": ''
}

QUERY = '''
{
  txs_queue(where: {block: {_lte: 13128900}}) {
    cyber
    eul
  }
}
'''