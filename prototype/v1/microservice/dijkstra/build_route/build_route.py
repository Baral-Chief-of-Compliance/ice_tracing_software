from app import Blueprint, jsonify, request
from app.use_db import map
from app.use_db import generate_route_db
import json
import build_route.route_building_area as route_building_area
import build_route.create_graph as create_graph
import build_route.create_src_dest as create_src_dest
import build_route.dijkstra as dijkstra
from build_route.convert_path_to_geojson import convert


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

        #использоваться будет это, но пока из файла
        # map_form_bd = map.get_map()
        #
        # json_map = json.loads(map_form_bd[0])

        with open("data/map_test.json") as file:
            json_map = json.load(file)

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

        start, goal = create_src_dest.create_src_dest(area)

        path = dijkstra.dijkstra(graph, start, goal)

        polyline_for_ymap = convert(path)

        json_path = json.dumps(polyline_for_ymap)

        generate_route_db.add_route(id_rt, json_path)

        return jsonify("path is build")
