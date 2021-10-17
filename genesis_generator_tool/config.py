# For genesis generator
BOOT_DENOM = "boot"
CYB_DENOM = '2cyb'

FILES = [
    ('multisigs.csv', 'multisigs'),
    ('bostrom_lifetime.csv', 'pre_bostrom_heroes'),
    ('comm_pool_rewards.csv', 'comm_pool'),
    ('cyberdbot_sergey.csv', 'cyberd_bot_sergey'),
    ('delegation.csv', 'delegation'),
    ('euler4_rewards.csv', 'euler-4'),
    ('inventors.csv', 'inventors'),
    ('investors.csv', 'investors'),
    ('lifetime_rewards.csv', 'lifetime'),
    ('load.csv', 'load'),
    ('port.csv', 'port'),
    ('relevance.csv', 'relevance'),
    ('sergandmyselfrewards.csv', 'sergeandmyself_rewards'),
    ('takeoff.csv', 'takeoff'),
    ('vladimirrewards.csv', 'posthuman_rewards'),
]

SUPPLY = 1_000_000_000_000_000

NETWORK_GENESIS_PATH = './data/network_genesis.json'