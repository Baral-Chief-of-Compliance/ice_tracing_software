from route_building_area import build
import json


with open("map.json", "r") as file:
    map_ = json.load(file)

width = len(map_)
length = len(map_[0])

start_longitude = 38.831525324316004
start_latitude = 68.91316126089126

end_longitude = 64.89570320937713
end_latitude = 74.67013839379428

build(map_, width, length, start_longitude, start_latitude, end_longitude, end_latitude)

with open("check_map.json", "w") as file:
    json.dump(map_, file)
