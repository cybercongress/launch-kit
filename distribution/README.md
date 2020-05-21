# Distribution

At first glance, the distribution looks pretty complex. This is not true. The main object of the successful launch PoS network is nice genesis distribution. You can find below the table with all the distribution parameters. To avoid confusion decided to use two pairs of tokens monikers in the testnet and the mainnet. Since different tasks following by the testnet and the mainnet the distribution different too. Anyway, the trend of allocating to communities as many tokens as possible follows in both cases.

## Distribution params

(Please see explanatory notes below the table)

| Parameters                             | `euler-6`   | `cyber`    |Notes|
|:----------------------------------|:-----------:|:----------:|:----:|
|*Distribution params*|
| Foundation contract address      | https://mainnet.aragon.org/#/eulerfoundation/0xd84469ecd96825c956d7ae8b072209ca89ae37e2/ | https://mainnet.aragon.org/#/cybercongress/0xa0a55e68dc52b47f8a9d5d05329fab5bdabffb14 | DAO |
| **Foundation token**             | **GOL**   | **THC**  | **ERC20 token in Aragon DAO**  |
| Distr to ETH Game of Thrones         | 1 TGOL  | 100 TTHC | Distribution of gov. tokens for Game of Thrones auction to the ETH community  |
| Auction distr                    | 6 TGOL  | 500 TTHC | Amount of gov. tokens allocated to the auction  |
| cyber~Congress distr             | 8 TGOL   | 100 TTHC  | Amont of gov. tokens allocated to cyber~Congress (inventors, team)   |
| Auction distr                    | 6 TGOL  | 600 TTHC | Amount of gov. tokens allocated to the auction  |
| cyber~Congress distr             | 8 TGOL   | 150 TTHC  | Amont of gov. tokens allocated to cyber~Congress (inventors, team)   |
| **Chain token**                  | **EUL**   | **CYB**  | **Chain liquid token**  |
| Cosmos gift                      | 10 TEUL   | 10 TCYB  | Chain token gift to the Cosmos community. Each address on block 1110000 entitlted to a gift according to [distribution]() |
| Ethereum gift                    | 80 TEUL   | 80 TCYB  | Chain token gift to the Ethereum community. 99.7% of addresses on block 8080808 are entitiled to a gift according to [distribution]() |
| Urbit gift                      | 10 TEUL   | 10 TCYB  | Chain token gift to the Urbit community |
| Validators euler-4 rewards       | 15 TEUL  | 5 TCYB | For validating during `euler-4`. Calculated per lifetime |
| Takeoff funding                  | 100 TEUL   | 100 TCYB  | Tokens allocated to takeoff funding |
| Relevance discipline            | NaN   | 20 TCYB  | Tokens allocated for Game of Links relevance discipline |
| Load discipline            | NaN   | 10 TCYB  | Tokens allocated for Game of Links load discipline |
| Delegation discipline            | NaN   | 5 TCYB  | Tokens allocated for Game of Links delegation discipline |
| Lifetime discipline            | NaN   | 3 TCYB  | Tokens allocated for Game of Links lifetime discipline |
| Community pool, GoL bounty       | 2 TEUL    | 2 TCYB   | Amount of tokens in the community pool at the start |
| Full validator set extra rewards | NaN   | 5 TCYB  | Extara reward to validators if the set of active validators will reach 146 and will last for a period of 10,000 blocks |
| Cosmos Game of Thrones            | 1 TEUL  | 100 TCYB | Chain tokens |
| Cosmos Game of Thrones            | 1 TEUL  | NaN | Chain tokens |
| **SUM**                          | 233 TEUL | 1000 TCYB|  |
|*Takeoff funding params*|
| Cosmos multisig address | cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a | cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a | Congress multisig address for atoms funding|
| Desired Atom funding             | 300,000 | NaN | The maximum amounts of desired ATOMs for funding|
| Distribution function | proportionally donated | f(x) = 40 * x + 1000 |
| Open funding                     | by proposal | - | The community will decide when funding will begin|
| Max. funding duration              | 146 days | - | Funding duration if 300,000 ATOMs will not be donated |
|*Auction contract params*|
| Contract address        | https://mainnet.aragon.org/#/eulerfoundation/0x0b1f54be915e77d9bf14268f94f8a26afab11296/ | ?                  | Contract address with allocated tokens |
| Open time               | with `euler-5` launch  | with `cyber` launch| The time of start of round `0` of the auction |
| Created on first day        | 100 TGOL               | 100 TTHC           | Amount of tokens allocated to round `0`|
| Starting time              | open_time + 240h       | open_time + 504h   | The time of start of round 1 |
| Number of rounds        | 49 + 1                 | 500 + 1            | Round zero + daily rounds |
| Created per day          | 8.16326531 TGOL        | 1 TTHC    | Amount of tokens allocated to each daily round|

\* -  the `x` the is amount of ATOMs funded for the current moment <br>
\ - distr. = distribution | gov. = governance <br>
\ - `Foundation token` refers to the Aragon entity that is in charge of the donated ETH as per the [protocol White paper](https://github.com/cybercongress/cyber/blob/master/main.tex). The Aragon DAO is responsible for on-chain governance. Please see out paper for more information <br>
\ - `Chain token` refers to the main token of the cyber protocol. It is used for staking, bandwith and for ranking. Please see protocol paper for more inforamtion.

## Workflow

PRs

For correct work of `genesis_generator_tool` is necessary to fill `cyber_distribution.json` file with groups for distributing. After it has done, necessary to fill `manual_distribution.json` with addresses of groups are excluded from automatic distribution. Check twice, the sum of addresses balances in  `manual_distribution.json` by the group should be equal with the group amount in `cyber_distribution.json`.
