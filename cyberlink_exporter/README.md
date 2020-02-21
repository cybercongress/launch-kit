# Cyberlinks exporter

This tool for export cyber links from the network to `cyberlinks.json` file. After succsessful export you can add IPLD structure to easy availability to links by account. 

Just fill the `config.py` file with necessary block `HEIGHT`, and your `hasura` credentials, after that run:

```bash
python exporter.py
```

The output file will contain addresses and array of links by this addresses such like:

```json
{
    "address0": 
        [
            {
                "from": "Qm11...", 
                "to": "Qm12..."
            },
             {
                "from": "Qm21...", 
                "to": "Qm22..."
            }
        ],
    .
    .
    . 
    "addressN": 
        [
            {
                "from": "Qm11...", 
                "to": "Qm112..."
            }
        ]
}
```

You can put it in IPLD structure by following command:

```bash
ipfs dag put cyberlinks.json
```

And explore it by the API:

```
http://127.0.0.1:5001/api/v0/dag/get?arg=<HASH>
```

And by address:

```
http://127.0.0.1:5001/api/v0/dag/get?arg=<HASH>/<address>
```