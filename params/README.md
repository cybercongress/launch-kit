# Genesis Parameters

A list of subjective parameter choices with reasons for their recommendation.


## cyberd parameters

| Param                 | `euler-4`     | `euler-6`    | `cyber`      |    Notes                                         |
|:-----------------------|:---------------:|:--------------:|:--------------:|:-------------------------------------------:|
| *Staking Module*                                                                                                                  |
| unbonding_time        | 21 days       | 5 days      | 21 days      |Duration time for unbonding                                   |
| max_validators        | 146           | 146          | 146          |Maximum number of active validators set                      |
| bonded_coin_denom     | cyb           | eul          | cyb          |The bonded coin denom.                                        |
| *Slashing module* |
| signed_blocks_window | 240         | 300        | 300        | The window for signing blocks  |
| min_signed_per_window | 0.80       | 0.70        | 0.70        | The fraction of signed blocks per window to be an active validator |
| downtime_jail_duration | 0 min | 30 min | 30 min | Time duration before unjail transaction available |
| slash_fraction_double_sign | 0.05| 0.02 |0.02 | Slashing for double sign |
| slash_fraction_downtime | 0.001| 0.0001|0.0001| Slashing for downtime |
|*Minting Module*    |
| inflation             | 0.07          | 0.03         | 0.03         |The initial annual inflation rate                                |
| inflation_max         | 0.20          | 0.15         | 0.15         |The maximum annual inflation rate                                |
| inflation_min         | 0.07          | 0.01         | 0.01         |The minimum annual inflation rate                                |
| inflation_rate_change | 0.13          | 0.13         | 0.13         |The rate at which the inflation rate changes                     |
| goal_bonded           | 0.67          | 0.88         | 0.88         |A point of inflation change sign                           |
| blocks_per_year       |31536000 (~1s) |6311520 (~5.5s) |6311520 (~5.5s) |The rate at which the inflation rate changes                     |
|*Distribution Module*                                                                                                              |
| community_tax         | 0.00          | 0.00         | 0.00         |The tax on inflation to the community pool                           |
| base_proposer_reward  | 0.01          | 0.01         | 0.01         |% of inflation allocated to block proposer                   |
| bonus_proposer_reward | 0.04          | 0.05         | 0.05         |% of bonus for block proposer for precommits                 |
| withdraw_addr_enabled | true          | true         | true         |Changing reward withdrawal addresses                         |
|*Governance Module*                                                                                                                |
| min_deposit           | 500000000000  | 10000000000 | 500000000000 |The minimum deposit to bring a proposal up for a vote        |
| max_deposit_period    | 2 days           | 5 days       | 21 days       |The duration at which a proposal can collect deposits        |
| voting_period         | 2 days           | 3 days       | 21 days       |The duration at which a proposal can be voted upon           |
| quorum                | 0.334         | 0.200        | 0.334        |A minimum quorum of bonded stake for voting                  |
| threshold             | 0.500         | 0.500        | 0.500        |A minimum threshold for the voting proposal to pass             |
| veto                  | 0.334         | 0.334        | 0.334        |A minimun of voting stake for vetoing a proposal                 |
|*Bandwidth Module*                                                                                                                 |
| recovery_period       | 16000(24.4h) blocks           | 16000(24.4h) blocks          | 16000(24.4h) blocks          |Full bandwidth recovery period                               |
| adjust_price_period   | 60 blocks            | 10 blocks           | 10 blocks          |How ofter the price is recalculated                              |
| base_credit_price     | 1.0           | 1.0          | 1.0          |The base bandwidth cost multiplier                           |
| desirable_bandwidth   | 200000000     | 2000000000    | 200000000    |The amount that all users on average can spend for recover period   |
| max_block_bandwidth   | 111111        | 250000       | 250000       |The maximum bandwidth in one block                        |
| link_msg_cost         | 100           | 100          | 100          |Link message cost                                            |
| tx_cost               | 300           | 300          | 300          |Transaction message cost                                     |
| non_link_msg_cost     | 500           | 500          | 500          |Non-link message cost                                        |
|*Rank Module*                                                                                                                      |
| calculation_period    | 100 blocks          | 5 blocks          | 100 blocks         |The window for rank calculation                              |
| damping_factor        | 0.85          | 0.85         | 0.85         |Link-through probability. Included to prevent sinks|
| tolerance             | 0.001         | 0.001        | 0.001        |Used  for  convergence  of PageRank vector                   |
