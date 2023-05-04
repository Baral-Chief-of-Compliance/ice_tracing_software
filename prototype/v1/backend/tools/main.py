from route_building_area import build, build_2
from create_graph import create
from dijkstra import dijkstra
from create_src_dest import create_src_dest
import sys
import json

sys.setrecursionlimit(2000)

with open("../ice/json/map_test.json", "r") as file:
    map_ = json.load(file)

width = len(map_)
length = len(map_[0])

start_longitude = 158.65804621207423
start_latitude = 76.10079999958671

end_longitude = 142.46414333404317
end_latitude = 72.99829163829796

iceclass = "Arc7"

area = build_2(map_, width, length, start_longitude, start_latitude, end_longitude, end_latitude)

# with open("area_check.txt", "w") as file:
#     for line in area:
#         file.write(str(line))
#         file.write("\n")

graph = create(area, iceclass)
src, dest = create_src_dest(area)
print(src)
print(dest)
dijkstra(graph, src, dest)


