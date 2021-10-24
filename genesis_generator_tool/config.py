# For genesis generator
BOOT_DENOM = "boot"
CYB_DENOM = 'tocyb'

FILES = [
    ('cybercongress.csv', 'cybercongress'),
    ('gift.csv', 'gift'),
    ('gol_comm_pool.csv', 'gol.comm_pool'),
    ('gol_delegation.csv', 'gol.delegation'),
    ('gol_lifetime.csv', 'gol.lifetime'),
    ('gol_load.csv', 'gol.load'),
    ('gol_posthuman.csv', 'gol.posthuman'),
    ('gol_relevance.csv', 'gol.relevance'),
    ('gol_sergeandmyself.csv', 'gol.sergeandmyself'),
    ('grants_cyberdbot.csv', 'grants.cyberdbot'),
    ('grants_init_implementation.csv', 'grants.init_implementation'),
    ('greatweb_foundation.csv', 'greatweb_foundation'),
    ('heroes_euler4.csv', 'heroes.euler4'),
    ('heroes_pre_bostrom.csv', 'heroes.pre_bostrom'),
    ('inventors.csv', 'inventors'),
    ('investors_genesis.csv', 'investors.genesis'),
    ('investors_port.csv', 'investors.port'),
    ('investors_takeoff.csv', 'investors.takeoff'),
    ('senate.csv', 'senate'),
]

SUPPLY = 1_000_000_000_000_000
NETWORK_GENESIS_PATH = './data/network_genesis.json'
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
