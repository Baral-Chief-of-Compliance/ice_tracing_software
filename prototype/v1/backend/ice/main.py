from test import create_ice
from ice_object_border import clear
from create_polygon import clean_map
import json
import sys
from threading import Thread

sys.setrecursionlimit(5000)


def create_geojson(map_, type_of_ice):
    map_ = clear(map_, type_of_ice)
    geojson = clean_map(map_, type_of_ice)

    with open(f"json/{type_of_ice}.json", "w") as file:
        json.dump(geojson, file)


with open("../tools/map.json", "r") as file:
    map_ = json.load(file)
#
#
map_ = create_ice(map_)
# map_ = clear(map_, "old_ice")
# with open("map_test.txt", "w") as file:
#     for line in map_:
#         file.write(str(line))
#         file.write("\n")


# map_point = [['.' for x in range(len(map_[0]))] for y in range(len(map_))]
#
# for y in range(len(map_point)):
#     for x in range(len(map_point[0])):
#         if map_[y][x]["type_of_ice"] == "old_ice":
#             map_point[y][x] = "#"
#
# with open("map_touch.txt", "w") as file:
#     for y in range(len(map_point)):
#         for x in range(len(map_point[0])):
#             file.write(map_point[y][x])
#
#         file.write("\n")

# geojson = clean_map(map_, "old_ice")
#
#
# with open("old_ice.json", "w") as file:
#     json.dump(geojson, file)


t1 = Thread(target=create_geojson, args=(map_, "first_year_ice"))
t2 = Thread(target=create_geojson, args=(map_, "young_ice"))
t3 = Thread(target=create_geojson, args=(map_, "old_ice"))
t4 = Thread(target=create_geojson, args=(map_, "nilas_ice"))
t5 = Thread(target=create_geojson, args=(map_, "fast_ice"))
t6 = Thread(target=create_geojson, args=(map_, "ice_field"))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
