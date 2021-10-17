# Genesis generator tool

This tool provides `genesis.json` file compilation from the next following files:

- [network_genesis.json](./data/network_genesis.json), the `genesis.json` file template with set parameters, but without accounts, community pool values and suuply.
- [bostrom_lifetime.csv](./data/bostrom_lifetime.csv), the rewards for `bostrom-testnets` [supporting](../pre_bostrom_lifetime/README.md)
- [comm_pool_rewards.csv](./data/comm_pool_rewards.csv), the [community pool rewards](../gol_rewards/README.md) during `euler` testnets, excluding evangelism program
- [cyberdbot_sergey.csv](./data/cyberdbot_sergey.csv), an extra gift for [cyberd telegram bot](https://github.com/Snedashkovsky/cyberdBot) users
- [delegation.csv](./data/delegation.csv), the [delegation rewards](../gol_rewards/README.md) of the Game of Links during `euler` testnets
- [euler4_rewards.csv](./data/euler4_rewards.csv), the [lifetime reards](../gol_rewards/README.md) during `euler-4`
- [inventors.csv](./data/inventors.csv), investor shares
- [investors.csv](./data/investors.csv), inventor shares
- [lifetime_rewards.csv](./data/lifetime_rewards.csv), the [lifetime reards](../gol_rewards/README.md) during `euler-5-6`
- [load.csv](./data/load.csv), the [load rewards](../gol_rewards/README.md) of the Game of Links during `euler` testnets
- [multisigs.csv](./data/multisigs.csv), cybercongress, gift and euler_foundation multisig accounts
- [port.csv](./data/port.csv), all [port visitors rewards](../port_migration/README.md)
- [relevance.csv](./data/relevance.csv), the [relevance rewards](../gol_rewards/README.md) of the Game of Links during `euler` testnets
- [sergandmyselfrewards.csv](./data/sergandmyselfrewards.csv), evangelism program rewards
- [takeoff.csv](./data/takeoff.csv), all [takeoff donors](../takeoff_distribution/README.md)
- [vladimirrewards.csv](./data/vladimirrewards.csv), special gift from posthuman

As the output of this script is generated [genesis.json](./data/genesis.json) file ready for signing. Also, the output is:

- [categorized_result.csv](./data/categorized_result.csv) the table with accs by categories
- [final_result.csv](./data/final_result.csv) the table with final result of calculations
- [genesis.csv](/data/genesis.csv) the table with grouped by agent balances