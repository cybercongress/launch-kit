from string import Template


HEADERS = {
    'content-type': 'application/json',
    "authorization": ''
  }

TOP_1000_ON_BLOCK = Template('''{
    relevance(where: {height: {_eq: $block}}, order_by: {rank: desc}) {
        object,
        rank
    }
}''')

STAKING_ON_BLOCK = Template('''{
  staking(where: {height: {_eq: $block}}) {
    operator_address
    tokens
  }
}''')

PRECOMMITS_ON_BLOCK = '''{
    pre_commits_final {
        consensus_pubkey
        precommits
  }
}'''
