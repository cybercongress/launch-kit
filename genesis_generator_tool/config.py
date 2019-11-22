from collections import OrderedDict

# For genesis generator
DENOM = "eul"
VALIDATORS_PATH_CSV = "./data/validators.csv"
CSV_DISTRIBUTIONS = OrderedDict([
    ("cosmos_drop", "./data/cosmos.csv"),
    ("ethereum_drop", "./data/ethereum.csv")
])
DISTRIBUTION_PATH = "./data/cyber_distribution.json"
MANUAL_DISTRIBUTION_PATH = "./data/manual_distribution.json"
GENESIS_EXAMPLE_PATH = "./data/network_genesis.json"
GENERATED_GENESIS_PATH = "./data/genesis.json"
DIFFERENCE_THRESHOLD = 0.0001