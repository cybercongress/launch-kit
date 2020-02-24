# Launch kit

An awesome must-have toolkit and a protocol for the Genesis launch. This toolkit provides a launch protocol for cosmos-based networks, recommended workflow and necessary tools for genesis.json compilation. Also, it contains a crisis protocol.

## ToC

- [Launch protocol](#launch-protocol)
- [Workflow](#workflow)
- [Tools](#tools)
- [Network params](#network-params)
- [Distribution params](#distribution-params)
- [Points of truth](#points-of-truth)

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

## Workflow

1. Develop your distribution for the launch. This is the most important step in this guide. What is the total genesis supply?
 Which communities should be involved? How to distribute tokens? What's the method for distribution you want to use? How many tokens you want to distribute to the foundation, team, donors, inventors and so on. Our example you can see at [distribution](./distribution/README.md) directory.

2. According to your distribution set up the `cyber_distribution.json` and `manual_distribution.json` files with necessary values. More about that at  [distribution](./distribution/README.md) directory. 

3. Set parameters for the network. At the [params](./params/README.md) directory you can open a discussion for the great params decision. Put all params inside `network_genesis.json`. 

4. Select a set of tools for genesis accounts preparation. This story about communities gifts, if your distribution includes the gifts for communities (like ours). There are two ways to include the group of addresses in the genesis file: 

- With genesis-generator-tool built-in method (quadratic function)
- With custom method

In the first case, you just need a `.csv` file with addresses and native chain balances. The genesis-generator tool will parse distribution files and apply the quadratic function to this group. 

> Notice. The addresses should be converted into the your-network format. For details visit provided [converter].

In the second case, you can calculate the balances as you want, and the genesis generator tool just inserts it in the right format. But you should carry about the distribution sum by yourself. This sum should compare with value at `cyber_distribution.json`. More technical details at the [genesis-generator-tool](./genesis-generator-tool/README.md). 

5. After you prepared all the files you need to move it to `genesis-generator-tool/data` and start the genesis generation.


## Tools

- The Game rewards tools
- ETH and Cosmos to Cyber converter
- ETH gift distributor
- Cosmos gift distributor
- Urbit gift distributor
- Genesis generator
- Data exporters

## Network params

The network paramas available at `params` [README](/params/README.md)

## Distribution params

The distribution paramas available at `distribution` [README](/distribution/README.md)

---

## Points of truth

|File name | Description | IPFS hash | 
| ---------|-------------|-----------|
| cosmos.csv | cosmos network balances state at block 1110000 |  QmcgfjcNwucHrSrWFNxKGYLjLouedYjyeP3hRrqD6P8m9K |
| ethereum.csv | ethereum network balances state at block 8080808, exclude contracts and addresses without at least one outgoing transaction | QmVCMwK3273Wb4gddzmxiitquCe844Qe63SWVyWFA8gEsT | 
| galaxies_balance.csv | galaxies balances on non-contract addresses with at least one outgoing transaction. At 9110129 block state | QmR7nbMZDrQE5wLoUhgKJ6pZiUkCyJ4bCfgDEyWGfH3SvJ |
| stars_balance.csv | stars balances on non-contract addresses with at least one outgoing transaction. At 9110129 block state | QmUkXZcHB9L3cg2uqMC5ejkCaD3eWsZRmyuWtdATxZUMKj |
| planets_balance.csv | planets balances on non-contract addresses with at least one outgoing transaction. At 9110129 block state | QmZjc2KEQMpvK3dudsyar1Qzq6e4M5ds3CCteUXbne6zxs | 