# Genesis Parameters

Many genesis fields are self-evident, null, or uncontroversial (e.g. gas prices, which are chosen for spam prevention).

Here the more subjective parameter choices are documented with the reasons behind their recommendation.

Note that all durations are specified in nanoseconds.

## cyberd parametrs

| Param                 | `euler-4` | `euler-5` | `cyber`  |                                        |
|-----------------------|----------------------|-----------|----------|----------------------------------------|
| *Staking Module*                                                                                               |
| unbonding_time        | 3 weeks              |3 weeks               |          |time duration of unbonding              |
| max_validators        | 146                  |146                   |          |maximum number of active validators set |
| bonded_coin_denom     | cyb                  |eul                   |          |the bonded coin denom                   |
| *Minting Module*        |                      |                      |          |                                        |
| inflation             | 0.07                 | 0.03                |                | initial annual inflation rate |
| inflation_max         | 0.20                 | 0.15                ||maximum annual inflation rate            |
| inflation_min         | 0.07                 | 0.01                ||minimum annual inflation rate            |
| inflation_rate_change | 0.13                 | 0.13                ||rate at which the inflation rate changes |
| goal_bonded           | 0.67                 | 0.88                ||the point of inflation change sign       |
| blocks_per_year       |31536000 (~1s) |6311520 (~5s) ||rate at which the inflation rate changes |

## Slashing Module

| Param                      | `euler-4` | `euler-5` |Comment                             |
|----------------------------|---------- |-----------|------------------------------------|
| max_evidence_ag            | 3 weeks   | 3 week    |the maximum age of evidence         |
| signed_blocks_window       | 1800      | 240       |the rolling window for uptime       |
| min_signed_per_window      | 0.42      | 0.80      |minimum signed blocks in the window |
| downtime_jail_duration     | 0s        | 0s        |the time before unjail is possible  |
| slash_fraction_double_sign | 0.20      | 0.05      |slashing for double-sign            |
| slash_fraction_downtime    | 0.001     |0.0005     |slashing for downtime               |

## Distribution Module

| Param                 | `euler-4` | `euler-5`           |Comment                                      |
|-----------------------|-----------|---------------------|---------------------------------------------|
| community_tax         | 0.00      | 0.10                |tax on inflation to community pool           |
| base_proposer_reward  | 0.01      | 0.01                |% of inflation allocated to block proposer   |
| bonus_proposer_reward | 0.04      | 0.05                |% of bonus for block proposer for precommits |
| withdraw_addr_enabled | true      | true                |changing reward withdrawal addresses         |

## Governance Module

| Param              | `euler-4`    | `euler-5`    |Comment                                                          |
|--------------------|--------------|--------------|-----------------------------------------------------------------|
| min_deposit        | 500000000000 | 500000000000 |the minimum deposit to bring a proposal up for a vote            |
| max_deposit_period | 48h          | 1 week       |the duration in which a proposal can collect deposits            |
| voting_period      | 48h          | 1 week       |the duration in which a proposal can be voted upon               |
| quorum             | 0.334        | 0.334        |a minimum quorum of 40% of bonded stake must vote on a proposal  |
| threshold          | 0.500        | 0.500        |over half the voting stake must vote in favor of a proposal      |
| veto               | 0.334        | 0.334        | 1/3 of voting stake vetoing a proposal prevents it from passing |

## Bandwidth Module

| Param               | `euler-4`    | `euler-5`    |Comment                                                          |
|---------------------|--------------|--------------|-----------------------------------------------------------------|
| recovery_period     | 24h          | 24h          |from 0 to max recovery period                                    |
| adjust_price_period | 1m           | 1m           |how ofter price is recalculated                                  |
| base_credit_price   | 1.0          | 1.0          |a minimum quorum of 40% of bonded stake must vote on a proposal  |
| desirable_bandwidth | 200000000    | 200000000    |over half the voting stake must vote in favor of a proposal      |
| max_block_bandwidth | 111111       | 111111       | 1/3 of voting stake vetoing a proposal prevents it from passing |
| link_msg_cost       | 100          | 100          |the minimum deposit to bring a proposal up for a vote            |
| tx_cost             | 300          | 300          | 1/3 of voting stake vetoing a proposal prevents it from passing |
| non_link_msg_cost   | 500          | 500          | 1/3 of voting stake vetoing a proposal prevents it from passing |

## Rank Module

| Param               | `euler-4`    | `euler-5`    |Comment                                                         |
|---------------------|--------------|--------------|----------------------------------------------------------------|
| calculation_period  | 100          | 100          |the number of blocks defined for graph full recalculation       |
| damping_factor      | 0.85         | 0.85         |                                                                |
| tolerance           | 0.001        | 0.001        |                                                                |
