from route_building_area import build
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

start_longitude = 38.831525324316004
start_latitude = 68.91316126089126

end_longitude = 64.89570320937713
end_latitude = 74.67013839379428

iceclass = "Ice1"

area = build(map_, width, length, start_longitude, start_latitude, end_longitude, end_latitude)

# with open("area_check.txt", "w") as file:
#     for line in area:
#         file.write(str(line))
#         file.write("\n")

graph = create(area, iceclass)
src, dest = create_src_dest(area)
print(src)
print(dest)
dijkstra(graph, src, dest)


