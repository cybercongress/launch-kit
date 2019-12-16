from web3 import Web3
from progressbar import ProgressBar
from google.cloud import bigquery
from tqdm import tqdm
from config import *
import pandas as pd

pbar = ProgressBar()

web3 = Web3(Web3.HTTPProvider(ETH_NODE_RPC))
contract = web3.eth.contract(address=AZIMUTH_CONTRACT_ADDRESS, abi=AZIMUTH_CONTRACT_ABI)

def run_sql(sql):
    client = bigquery.Client.from_service_account_json(GOOGLE_KEY_PATH)
    query = client.query(sql)
    result = query.result()
    return result

def collect_points(points_list):
    galaxies = {}
    stars = {}
    planets = {}
    for point in pbar(points_list):
        owner = str(contract.functions.getOwner(int(point)).call())
        point_size = contract.functions.getPointSize(int(point)).call()
        if point_size == 0:
            if owner in galaxies.keys():
                current_galaxies_count = galaxies[owner]
                current_galaxies_count += 1
                galaxies[owner] = current_galaxies_count
            else:
                galaxies[owner] = 1
        elif point_size == 1:
            if owner in stars.keys():
                current_stars_count = stars[owner]
                current_stars_count += 1
                stars[owner] = current_stars_count
            else:
                stars[owner] = 1
        else:
            if owner in planets.keys():
                current_planets_count = planets[owner]
                current_planets_count += 1
                planets[owner] = current_planets_count
            else:
                planets[owner] = 1
    return galaxies, stars, planets

def token_allocation(urbit_points):
    galaxies, stars, planets = collect_points(urbit_points)
    sum_galaxies = sum(galaxies.values())
    sum_stars = sum(stars.values())
    sum_planets = sum(planets.values())
    for owner in galaxies:
        galaxies[owner] = galaxies[owner] / sum_galaxies * GALAXIES_ALLOC

    for owner in stars:
        stars[owner] = stars[owner] / sum_stars * STARS_ALLOC

    for owner in planets:
        planets[owner] = planets[owner] / sum_planets * PLANETS_ALLOC
    return galaxies, stars, planets

def saving_to_csv(urbit_allocation):
    galaxies, stars, planets = urbit_allocation
    galaxies_df = pd.DataFrame.from_dict(galaxies, orient='index')
    stars_df = pd.DataFrame.from_dict(stars, orient='index')
    planets_df = pd.DataFrame.from_dict(planets, orient='index')
    frames = [galaxies_df, stars_df, planets_df]
    urbit_df = pd.concat(frames)
    urbit_df.to_csv('./data/urbit.csv', header=False)

print("Collecting all points from ethereum public dataset")
result = run_sql(URBIT_POINTS_SQL)
results = [dict(row) for row in tqdm(result, total=result.total_rows)]
urbit_points = [x['value'] for x in results]

print("Start to group point holders")
urbit_points = collect_points(urbit_points)

print("allocate tokens by groups")
print("galaxies:", GALAXIES_ALLOC)
print("stars:", STARS_ALLOC)
print("planets:", PLANETS_ALLOC)

urbit_allocation = token_allocation(urbit_points)

print("saving to ./data/urbit.csv")
saving_to_csv(urbit_allocation)
print("done")












