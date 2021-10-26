# Genesis generator tool

This tool provides `genesis.json` file compilation from the next following files:

- [network_genesis.json](../params/network_genesis.json), the `genesis.json` file template with set parameters, but without accounts, community pool values and suuply.
- [manual_distribution.csv](../manual/manual_distribution.csv), this file is filled with inventors, genesis investors, senate and multisig accounts.
- [bostrom_lifetime.csv](../pre_bostrom_lifetime/heroes_pre_bostrom.csv), the rewards for `bostrom-testnets` supporting
- [comm_pool_rewards.csv](../game_of_links/gol_comm_pool.csv), the community pool rewards during `euler` testnets, excluding evangelism program
- [cyberdbot_sergey.csv](../manual/grants_cyberdbot.csv), an extra gift for [cyberd telegram bot](https://github.com/Snedashkovsky/cyberdBot#data-for-the-bostrom-genesis) users
- [delegation.csv](../game_of_links/gol_delegation.csv), the delegation rewards of the Game of Links during `euler` testnets
- [euler4_rewards.csv](../game_of_links/heroes_euler4.csv), the lifetime rewards during `euler-4`
- [lifetime_rewards.csv](../game_of_links/gol_lifetime.csv), the lifetime rewards during `euler-5-6`
- [load.csv](../game_of_links/gol_load.csv), the load rewards of the Game of Links during `euler` testnets
- [port.csv](../eth_fundraiser/investors_port.csv), all port visitors rewards
- [relevance.csv](../game_of_links/gol_relevance.csv), the relevance rewards of the Game of Links during `euler` testnets
- [gol_sergeandmyself.csv](../game_of_links/gol_sergeandmyself.csv), evangelism program rewards
- [investors_takeoff.csv](../takeoff_distribution/investors_takeoff.csv), all [takeoff donors](../takeoff_distribution/README.md)
- [gol_posthuman.csv](../game_of_links/gol_posthuman.csv), special gift from posthuman

As the output of this script is generated [genesis.json](./data/genesis.json) file ready for signing. Also, the output is:

- [categorized_result.csv](../distribution/categorized_result.csv) the table with accs by categories
- [Audience Pivot](../distribution/audience_pivot.csv) contains summary audience categorization
- [Discipline Pivot](../distribution/discipline_pivot.csv) contains summary discipline categorization
- [genesis.json](../distribution/discipline_pivot.csv) ready for signing Genesis file

## Usage

1. Install packages

```bash
pip3 install -r requirements.txt
```

2. Run

```bash
python3 genesis_generator.py
```