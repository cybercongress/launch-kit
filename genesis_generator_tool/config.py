# For genesis generator
BOOT_DENOM = "boot"
CYB_DENOM = 'tocyb'

FILES = [
    ('../distribution/manual_distribution.csv', ''),
    ('../gol_rewards/heroes_euler4.csv', 'heroes.euler4'),
    ('../takeoff_distribution/investors_takeoff.csv', 'investors.takeoff'),
    ('../gol_rewards/gol_comm_pool.csv', 'gol.comm_pool'),
    ('../port_migration/investors_port.csv', 'investors.port'),
    ('../pre_bostrom_lifetime/heroes_pre_bostrom.csv', 'heroes.pre_bostrom'),
    ('../gol_rewards/gol_delegation.csv', 'gol.delegation'),
    ('../gol_rewards/gol_lifetime.csv', 'gol.lifetime'),
    ('../gol_rewards/gol_load.csv', 'gol.load'),
    ('../gol_rewards/gol_relevance.csv', 'gol.relevance'),
    ('../gol_rewards/gol_sergeandmyself.csv', 'gol.sergeandmyself'),
    ('../gol_rewards/gol_posthuman.csv', 'gol.posthuman'),
    ('../distribution/grants_cyberdbot.csv', 'grants.cyberdbot')
]

SUPPLY = 1_000_000_000_000_000
NETWORK_GENESIS_PATH = '../params/network_genesis.json'
RESULTS_PATH = '../distribution/'
COMMUNITY_POOL_ACC = 'bostrom1jv65s3grqf6v6jl3dp4t6c9t9rk99cd8yvs0hc'


def get_base_account(account_number, address):
    return {
            "@type": "/cosmos.auth.v1beta1.BaseAccount",
            "account_number": account_number,
            "address": address,
            "pub_key": None,
            "sequence": "0"
        }


def get_module_account(account_number, address):
    return {
        "@type": "/cosmos.auth.v1beta1.ModuleAccount",
        "base_account": {
            "account_number": account_number,
            "address": address,
            "pub_key": None,
            "sequence": "0"
        },
        "name": "distribution",
        "permissions": []
    }


def get_base_balance(address, amount):
    return {
    "address": address,
    "coins": [
        {
            "amount": amount,
            "denom": BOOT_DENOM
        },
        {
            "amount": amount,
            "denom": CYB_DENOM
        }
    ]
}
