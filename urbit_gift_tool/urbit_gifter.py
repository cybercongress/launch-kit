from config import *
import pandas as pd
import csv

def token_allocation(urbit_points):
    galaxies, stars, planets = urbit_points
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

galaxies = pd.read_csv('./data/galaxies.csv', header=None, index_col=0, squeeze=True).to_dict()
stars = pd.read_csv('./data/stars.csv', header=None, index_col=0, squeeze=True).to_dict()
planets = pd.read_csv('./data/planets.csv', header=None, index_col=0, squeeze=True).to_dict()

print(galaxies)

urbit_points = galaxies, stars, planets

print("allocate tokens by groups")
print("galaxies:", GALAXIES_ALLOC)
print("stars:", STARS_ALLOC)
print("planets:", PLANETS_ALLOC)

urbit_allocation = token_allocation(urbit_points)

print("saving to ./data/urbit.csv")
saving_to_csv(urbit_allocation)
print("done")