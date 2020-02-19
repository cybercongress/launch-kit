# Launch kit

An awesome must-have toolkit and a protocol for the Genesis launch. This toolkit provides a launch protocol for cosmos-based networks, recommended workflow and necessary tools for genesis.json compilation. Also, it contains a crisis protocol.

## Launch protocol

In general, the protocol has three zones:

- Genesis preparation
- Network and contracts running
- Finalization

The Genesis preparation zone is about collecting addresses for distribution, distribution parameters, network parameters, and genesis transactions. All collected data is integrating into `genesis.json` by the `network_genesis.json` template. 

Also, this zone is about setupping  DAO as a governance entity.

The network and contracts running zone is the stage between block #1 of the launch network and the latest block of the network. The latest block is defined by the result of the takeoff donation round. In other words: the latest block should be after all of pending DAO commitments. This zone is defined as a danger zone because of a possible fault risk of network, contracts, all both of them.

This zone contains three major events:

- Deploying the web app for interacting with the network and DAO functions
- Takeoff donation round starting
- Deploying the contracts for the Auction
- Tokens distribution

The finalization zone should be available only after tokens distribution (as pended commitment). The main event of this zone is mainnet preparations done.

![launch workflow](pic/launch_protocol_v2.png)

## Tools

- The Game rewards tools
- ETH and Cosmos to Cyber converter
- ETH gift distributor
- Cosmos gift distributor
- Urbit gift distributor
- Genesis generator
- Data exporters

## Chain params

The chain paramas available at `params` [README](/params/README.md)

## Distribution params

The distribution paramas available at `distribution` [README](/distribution/README.md)

---

## Points of truth

|File name | Description | IPFS hash | 
| ---------|-------------|-----------|
| cosmos.csv | cosmos network balances state at block 1110000 |  QmcgfjcNwucHrSrWFNxKGYLjLouedYjyeP3hRrqD6P8m9K |
| ethereum.csv | ethereum network balances state at block 8080808, exclude contracts and addresses without at least one outgoing transaction | QmVCMwK3273Wb4gddzmxiitquCe844Qe63SWVyWFA8gEsT | 
| galaxies_balance.csv | galaxies balances on non-contract addresses with at least one outgoing transaction. At ~9128000 block state | QmR7nbMZDrQE5wLoUhgKJ6pZiUkCyJ4bCfgDEyWGfH3SvJ |
| stars_balance.csv | stars balances on non-contract addresses with at least one outgoing transaction. At ~9128000 block state | QmUkXZcHB9L3cg2uqMC5ejkCaD3eWsZRmyuWtdATxZUMKj |
| planets_balance.csv | planets balances on non-contract addresses with at least one outgoing transaction. At ~9128000 block state | QmZjc2KEQMpvK3dudsyar1Qzq6e4M5ds3CCteUXbne6zxs | 