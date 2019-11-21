# Launch kit
The necessary toolkit and protocol for Genesis launch. 

## Launch protocol
![](launch_protocol_v2.png)

## Tools

- lifetime rewards tool
- load rewards tool
- staking rewards tool
- relevance rewards tool
- eth-cyber converter
- cosmos-cyber converter
- eth gifts distributor
- cosmos gifts distributor
- genesis generator

## The workflow

## Chain params

The chain paramas available at `params` [README](/params/README.md)

## Distribution params

| Param                            | `euler-5` | `cyber`  |Comment                                                   |
|----------------------------------|-----------|----------|----------------------------------------------------------|
| **foundation token**             | **GOL**   | **THC**  |**ERC20 token in Aragon DAO**  |
| Eth Game of Thrones distr        | 100 TGOL  | 100 TTHC |Gov tokens distribution to Game of Thrones auction for ETH community  |
| Auction distr                    | 500 TGOL  | 500 TTHC |Gov tokens allocated to auction  |
| cyber~Congress distr             | 97 TGOL   | 97 TTHC  |Gov tokens allocated to cyber~Congress (investors, inventors, team)   |
| **chain token**                  | **EUL**   | **CYB**  |**chain liquid token**  |
| cosmos gift                      | 10 TEUL   | 10 TCYB  |The chain tokens gift for cosmos community. Each address on block 1110000 have a gift according to [distribution]() |
| ethereum gift                    | 90 TEUL   | 90 TCYB  |The chain tokens gift for ethereum community. 99.7% of addresses on block 8080808 have a gift according to [distribution]() |
| validators euler-4 rewards       | 2.7 TEUL  | 2.7 TCYB |For validating in `euler-4`. Calculated by the lifetime |
| community pool                   | 0.3 TEUL  | 0.3 TCYB |Tokens in the community pool at the start |
| takeoff funding                  | 60 TEUL   | 60 TCYB  |Tokens, allocated to takeoff funding |
| game of Links rewards            | 25 TEUL   | 25 TCYB  |Tokens, allocated to game of links rewards |
| community pool, GoL bounty       | 5 TEUL    | 5 TCYB   | ? |
| full validator set extra rewards | 10 TEUL   | 10 TCYB  |Extara rewards for validators if the set of active validators will rich 146 and prolong untill 10,000 blocks |
| game of Throne cosmos            | 100 TEUL  | 100 TCYB |Chain tokens |
| **sum**                          | 1000 TEUL | 1000 TCYB|  |



## Takeoff funding params

| Param                            | `euler-5`    | `cyber`    |Comment                                                     |
|----------------------------------|--------------|--------------|----------------------------------------------------------|
| **foundation token**             | **GOL**      | **THC**      |**ERC20 token in Aragon DAO**                     |
| **foundation token**             | **GOL**      | **THC**      |**ERC20 token in Aragon DAO**                     |
| **foundation token**             | **GOL**      | **THC**      |**ERC20 token in Aragon DAO**                     |



## Auction contract params

| Param           | `euler-5`    | `cyber`    |Comment                                                     |
|-----------------|--------------|--------------|----------------------------------------------------------|
| openTime        | by proposal  | **THC**      |**ERC20 token in Aragon DAO**                             |
| createFirstDay  | **GOL**      | **THC**      |**ERC20 token in Aragon DAO**                             |
| startTime       | **GOL**      | **THC**      |**ERC20 token in Aragon DAO**                             |
| numberOfDays    | **GOL**      | **THC**      |**ERC20 token in Aragon DAO**                             |
| createPerDay    | **GOL**      | **THC**      |**ERC20 token in Aragon DAO**                             |
| foundation      | **GOL**      | **THC**      |**ERC20 token in Aragon DAO**                             |
