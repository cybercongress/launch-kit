# Genesis Parameters

Here the more subjective parameter choices are documented with the reasons behind their recommendation.


## cyberd parametrs

| Param                 | `euler-4`     | `euler-5`    | `cyber`      |                                                             |
|-----------------------|---------------|--------------|--------------|-------------------------------------------------------------|
| *Staking Module*                                                                                                                  |
| unbonding_time        | 3 weeks       | 3 weeks      | 3 weeks      |time duration of unbonding                                   |
| max_validators        | 146           | 146          | 146          |maximum number of active validators set                      |
| bonded_coin_denom     | cyb           | eul          | cyb          |the bonded coin denom                                        |
|*Minting Module*                                                                                                                   |
| inflation             | 0.07          | 0.03         | 0.03         |initial annual inflation rate                                |
| inflation_max         | 0.20          | 0.15         | 0.15         |maximum annual inflation rate                                |
| inflation_min         | 0.07          | 0.01         | 0.01         |minimum annual inflation rate                                |
| inflation_rate_change | 0.13          | 0.13         | 0.13         |rate at which the inflation rate changes                     |
| goal_bonded           | 0.67          | 0.88         | 0.88         |the point of inflation change sign                           |
| blocks_per_year       |31536000 (~1s) |6311520 (~5s) |6311520 (~5s) |rate at which the inflation rate changes                     |
|*Distribution Module*                                                                                                              |
| community_tax         | 0.00          | 0.10         | 0.10         |tax on inflation to community pool                           |
| base_proposer_reward  | 0.01          | 0.01         | 0.01         |% of inflation allocated to block proposer                   |
| bonus_proposer_reward | 0.04          | 0.05         | 0.05         |% of bonus for block proposer for precommits                 |
| withdraw_addr_enabled | true          | true         | true         |changing reward withdrawal addresses                         |
|*Governance Module*                                                                                                                |
| min_deposit           | 500000000000  | 500000000000 | 500000000000 |the minimum deposit to bring a proposal up for a vote        |
| max_deposit_period    | 48h           | 1 week       | 1 week       |the duration in which a proposal can collect deposits        |
| voting_period         | 48h           | 1 week       | 1 week       |the duration in which a proposal can be voted upon           |
| quorum                | 0.334         | 0.334        | 0.334        |a minimum quorum of bonded stake for voting                  |
| threshold             | 0.500         | 0.500        | 0.500        |a minimum threshold the voting for proposal pass             |
| veto                  | 0.334         | 0.334        | 0.334        |a minimun of voting stake vetoing a proposal                 |
|*Bandwidth Module*                                                                                                                 |
| recovery_period       | 24h           | 24h          | 24h          |full bandwidth recovery period                               |
| adjust_price_period   | 1m            | 1m           | 1m           |how ofter price is recalculated                              |
| base_credit_price     | 1.0           | 1.0          | 1.0          |the base bandwidth cost multiplier                           |
| desirable_bandwidth   | 200000000     | 200000000    | 200000000    |how much all users in average can spend for recover period   |
| max_block_bandwidth   | 111111        | 111111       | 111111       |the maximum of bandwidth in one block                        |
| link_msg_cost         | 100           | 100          | 100          |link message cost                                            |
| tx_cost               | 300           | 300          | 300          |transaction message cost                                     |
| non_link_msg_cost     | 500           | 500          | 500          |non-link message cost                                        |
|*Rank Module*                                                                                                                      |
| calculation_period    | 100           | 100          | 100          |the window for rank calculation                              |
| damping_factor        | 0.85          | 0.85         | 0.85         |is the link-through probability, is included to prevent sinks|
| tolerance             | 0.001         | 0.001        | 0.001        |used  for  convergence  of PageRank vector                   |
