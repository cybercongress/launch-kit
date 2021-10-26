# Bostrom genesis parameters [WIP]

| Module           	| Parameter                      	| Value        	| Network unit   | Network value |
|------------------	|--------------------------------	|--------------	|----------------|---------------|
| staking          	|                                	|              	|                |               |
|                  	| unbonding_time                 	| 4 days       	| seconds        | 345600s       |
|                  	| max_validators                 	| 92           	| count          | 92            |
|                  	| max_entries                    	| 10            | count          | 10            |
| resources         |                                	|              	|                |               |
|                  	| max_slots                      	| 8            	| count          | 8             |
|                  	| halving_period_volt_blocks      | 9M blocks (1.5y) | blocks        | 9000000       |
|                  	| halving_period_ampere_blocks    | 9M blocks (1.5y) | blocks        | 9000000       |
|                  	| base_investmint_period_volt     | 1 month      	| seconds        | 2592000       |
|                  	| base_investmint_period_ampere   | 1 month      	| seconds        | 2592000       |
|                  	| base_investmint_amount_volt     | 100 MHYDROGEN   | hydrogen       | 1000000000    |
|                   | base_investmint_amount_ampere   | 1 GHYDROGEN     | hydrogen       | 100000000     |
|                   | min_investmint_period           | 1 day           | seconds        | 86400         |
| mint              |                                	|              	|                |               |
|                  	| inflation                      	| 5%          	| share          | 0.05          |
|                  	| mint_denom                     	| boot         	| denom          | boot          |
|                  	| inflation_rate_change          	| 20%           | share          | 0.20          |
|                  	| inflation_max                  	| 15%          	| share          | 0.15          |
|                  	| inflation_min                  	| 3%           	| share          | 0.03          |
|                  	| goal_bonded                    	| 80%          	| share          | 0.80          |
| rank             	|                                	|              	|                |               |
|                  	| calculation_period             	| 5            	| blocks         | 5             |
|                  	| damping_factor                 	| 0.80         	| share          | 0.80          |
|                  	| tolerance                      	| 0.001        	| share          | 0.001         |
| bandwidth        	|                                	|              	|                |               |
|                  	| recovery_period                	| 16000 blocks 	| blocks         | 16000         |
|                  	| adjust_price_period            	| 5 blocks     	| blocks         | 5             |
|                  	| base_price                     	| 0.25         	| share          | 0.25          |
|                  	| base_load                     	| 0.10         	| share          | 0.10          |
|                  	| max_block_bandwidth            	| 25000         | amount         | 25000         |
| liquidity        	|                                	|              	|                |               |
|                  	| min_init_deposit_amount        	| 1000000       | amount         | 1000000       |
|                  	| init_pool_coin_mint_amount     	| 10000000      | amount         | 10000000      |
|                  	| pool_creation_fee              	| 1 GBOOT      	| boot           | 1000000000    |
|                  	| swap_fee_rate                  	| 0.3%         	| share          | 0.003         |
|                  	| withdraw_fee_rate              	| 0.3%         	| share          | 0.003         |
| gov              	|                                	|              	|                |               |
|                  	| min_deposit                    	| 1 GBOOT      	| boot           | 1000000000    |
|                  	| max_deposit_period             	| 1 Week       	| seconds        | 604800s       |
|                  	| voting_period                  	| 1 Week       	| seconds        | 604800s       |
|                  	| quorum                         	| 25.0%        	| share          | 0.25          |
|                  	| threshold                      	| 50%          	| share          | 0.5           |
|                  	| veto_threshold                 	| 25.0%        	| share          | 0.25          |
| dmn             	|                                	|              	|                |               |
|                  	| max_slots                      	| 4            	| amount         | 4             |
|                  	| max_gas                        	| 2.5M          | gas            | 2500000       |
|                  	| fee_ttl                        	| 50           	| amount         | 50            |
| grid            	|                                	|              	|                |               |
|                  	| max_routes                     	| 16          	| amount         | 16            |
| distribution     	|                                	|              	|                |               |
|                  	| community_tax                  	| 0%           	| share          | 0.00          |
|                  	| base_proposer_reward           	| 1%           	| share          | 0.01          |
|                  	| bonus_proposer_reward          	| 3%           	| share          | 0.03          |
| slashing         	|                                	|              	|                |               |
|                  	| signed_blocks_window           	| 8000  blocks  | blocks         | 8000          |
|                  	| min_signed_per_window          	| 75%          	| share          | 0.75          |
|                  	| downtime_jail_duration         	| 600 sec       | seconds        | 600s          |
|                  	| slash_fraction_double_sign     	| 5%           	| share          | 0.05          |
|                  	| slash_fraction_downtime        	| 0.01%        	| share          | 0.0001        |
| crisis           	|                                	|              	|                |               |
|                  	| constant_fee                   	| 10 MBOOT     	| boot           | 10000000      |
| wasm             	|                                	|              	|                |               |
|                  	| code_upload_access             	| Everybody    	| text           | Everybody     |
|                  	| instantiate_default_permission 	| Everybody    	| text           | Everybody     |
|                  	| max_wasm_code_size             	| 1200 KB       | bytes          | 1228800       |
| auth             	|                                	|              	|                |               |
|                  	| max_memo_characters            	| 1024         	| symbols        | 1024          |
|                  	| tx_sig_limit                   	| 7            	| amount         | 7             |
|                  	| tx_size_cost_per_byte          	| 20            | cost           | 20            |
| consensus_params 	|                                	|              	|                |               |
|                  	| max_bytes                      	| 4 MB        	| bytes          | 4194304       |
|                  	| max_gas                        	| 25M         	| gas            | 25000000      |
