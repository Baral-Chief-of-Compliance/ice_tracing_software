from app import Blueprint, jsonify, request
from app.use_db import map
from app.use_db import generate_route_db
import json
import build_route.route_building_area as route_building_area
import build_route.create_graph as create_graph
import build_route.create_src_dest as create_src_dest
import build_route.dijkstra as dijkstra


build_route = Blueprint('build_route', __name__)


@build_route.route('/build_route', methods=['POST'])
def build_route_inf():
    if request.method == 'POST':
        id_rt = request.json["id_rt"]

        start_point_longitude = request.json["start_point_longitude"]
        start_point_latitude = request.json["start_point_latitude"]

        end_point_longitude = request.json["end_point_longitude"]
        end_point_latitude = request.json["end_point_latitude"]

        iceclass = request.json["iceclass"]

        area_building_route = request.json["area_building_route"]

        map_form_bd = map.get_map()

        json_map = json.loads(map_form_bd[0])

        area = route_building_area.build_interval_route(json_map, area_building_route)

        area_width = len(area)
        area_length = len(area[0])

        area_y_next_point, area_x_next_point = route_building_area.nearest(
            area,
            area_width,
            area_length,
            end_point_longitude,
            end_point_latitude
        )

        area_y_start_point, area_x_start_point = route_building_area.nearest(
            area,
            area_width,
            area_length,
            start_point_longitude,
            start_point_latitude
        )

        area[area_y_start_point][area_x_start_point]["start"] = True
        area[area_y_next_point][area_x_next_point]["end"] = True

        generate_route_db.add_intermediate(
            id_rt,
            area[area_y_next_point][area_x_next_point]["longitude"],
            area[area_y_next_point][area_x_next_point]["latitude"]
        )

        graph = create_graph.create(area, iceclass)
        with open("graph_test.json", "w") as file:
            json.dump(graph, file)
        start, goal = create_src_dest.create_src_dest(area)

        dijkstra.dijkstra(graph, start, goal)

        # cur_node = goal
        #
        # print(f'\npath from {goal} to {start}: \n {goal} ', end="")
        # print("start: ", start)
        # print("goal: ", goal)
        # print(visited)
        # while cur_node != start:
        #     cur_node = visited[cur_node]
        #     print(f'---> {cur_node} ', end='')

        # with open("data/pathArc7.json", "r") as file:
        #     polyline_for_ymap = json.load(file)
        #
        # json_way = json.dumps(polyline_for_ymap)
        #
        # generate_route_db.add_route(id_rt, json_way)
        print("over")
        return "hello"