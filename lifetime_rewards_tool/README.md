# Validators analysis

## Requirements:

- [docker-compose](https://docs.docker.com/compose/install/)
- python 3
- running euler-4 network docker container (RPC should be available)

## Installation and startup

1. Set `NODE_HOST`, `NODE_PORT` and `THREADS` in `.env` file.

`NODE_HOST` is the IP address of `cyberd` node. The best option is to run the `cyberd` node on the same machine. In this case set `127.0.0.1`

`NODE_PORT` is the RPC port of your node. If you are running a `cyberd` node from docker, you can get a port from the `docker ps` command output. By default its `26657`

`THREADS` - the number of parallel threads of indexing. Default value is `4`. 

2. To run containers, use the command:
```bash
$ docker-compose up --build
```
Pulling and installation may require 10-15 minutes, depending on your internet connection

This command will start the crawler and prepare the notebook with calculations. 
To see the table with validators' balances and explanatory calculations, click this link: http://localhost:8888/notebooks/balances.ipynb. 

The token will be requested, it can be found in the output of the docker-compose command:
```
[I 00:15:36.448 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
notebook_1  | [C 00:15:36.448 NotebookApp] 
notebook_1  |     
notebook_1  |     Copy/paste this URL into your browser when you connect for the first time,
notebook_1  |     to login with a token:
notebook_1  |         http://(m-Inspiron-7577 or 127.0.0.1):8888/?token=903b1dd72d8b9c95c839c75162208a1a8147b270e6aa3208
```

The crawler may index blocks between 6-10 hours if `cyberd` runs on localhost. 

3. Optionally, you can run `jupiter notebook` separately. Go to `validators-investigation/data/notebook` and run `jupyter-notebook` (`jupyter-notebook` should be installed)

4. Follow steps in the `balances.ipynb`
