import os

# There are options that can be configured in .env file
NODE_HOST = os.environ["NODE_HOST"]
NODE_PORT = os.environ["NODE_PORT"]
FIRST_BLOCK = int(os.environ["FIRST_BLOCK"])
THREADS = int(os.environ["THREADS"])

# Probably, there is no need to touch this group of options
DATABASE = "cyberd"
CHUNK_SIZE = 1000