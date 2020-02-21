# Game rewards calculations

This tool for calculations the Game of Links results. 
In general, this tool makes queries to GraphQL API for getting all info according to the game. 

Just fill the `config.py` file with necessary block `HEIGHT`, and your `hasura` credentials, after that run:

```bash
python calculator.py
```

## Precommits 

The output of this part of the tool is `./data/precommits.csv` file with validators consensus pubkeys and the number of precommits. 