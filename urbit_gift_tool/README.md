# Urbit gift tool

The urbit gift tool parses all existed [Azimuth](https://etherscan.io/address/0x6ac07b7c4601b5ce11de8dfe6335b871c7c4dd4d) contract points (ERC721 tokens) and save them. After that, it checks the ownership of points by addresses and saves the result to `./data/galaxies.csv`,  `./data/galaxies.csv`, `./data/stars.csv`, and `./data/planets.csv` as like:

```bash
ethereum_address, amount
```

 The entities ownership decides at the current block, the number of entities decides at the asked block. 

After that, the tool allocates the gift tokens according to galaxies, stars and planets allocation proportionally.

## Usage

1. Fill the `google-big-query-key.example.json` with your credentials and rename it to `google-big-query-key.json`
2. Fill the `config.py` file with the next parameters:

```bash
DEFAULT_ETHEREUM_BLOCK =
GOOGLE_KEY_PATH = "google-big-query-key.json"
ETH_NODE_RPC = ""
GALAXIES_ALLOC =
STARS_ALLOC =
PLANETS_ALLOC =
```

3. Run the `urbit_address_parser.py`

```bash
python urbit_address_parser.py
```

4. Run the `urbit_gifter.py` 

```bash
python urbit_gifter.py
```

5. The output will be available at `./data/urbit.csv` with eth addresses and allocated tokens.