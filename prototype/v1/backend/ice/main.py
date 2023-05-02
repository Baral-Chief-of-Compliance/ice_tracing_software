from test import create_ice
import json

with open("../tools/map.json", "r") as file:
    map_ = json.load(file)


map_ = create_ice(map_)

