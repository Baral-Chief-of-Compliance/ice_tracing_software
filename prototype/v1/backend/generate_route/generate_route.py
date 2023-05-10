from app import Blueprint, jsonify, request, json
from app.tools import route_building_area
from app.tools import create_graph
from app.tools import create_src_dest
from app.tools import dijkstra


generate_route = Blueprint('generate_route', __name__)


@generate_route.route('/generate_route', methods=['POST'])
def generate():
    if request.method == 'POST':
        iceclass = request.json['iceclass']

        start_longitude = request.json['start_longitude']
        start_latitude = request.json['start_latitude']

        end_longitude = request.json['end_longitude']
        end_latitude = request.json['end_latitude']

        print(f"Ледовый класс: {iceclass} \n\n"
              f"Долгота исходного пункта: {start_longitude} \n"
              f"Широта исходного пункта: {start_latitude} \n\n"
              f"Долгота пункта назначения: {end_longitude}\n"
              f"Широта пункта назначения: {end_latitude}")

        return jsonify({
            "iceclass": iceclass,
            "start_longitude": start_longitude,
            "start_latitude": start_latitude,
            "end_longitude": end_longitude,
            "end_latitude": end_latitude
        })


@generate_route.route('/generate_area', methods=['POST'])
def define_square_area():
    if request.method == "POST":
        start_longitude = request.json["start_longitude"]
        start_latitude = request.json["start_latitude"]
        print(start_longitude)
        print(start_latitude)

        with open("data/map.json", "r") as file:
            map_ = json.load(file)

        width = len(map_)
        length = len(map_[0])

        y, x = route_building_area.nearest(map_, width, length, start_longitude, start_latitude)

        print(y, x)

        right_top_area = map_[y - 2][x - 5]
        left_top_area = map_[y - 2][x + 5]
        left_bottom_area = map_[y + 2][x + 5]
        right_bottom_area = map_[y + 2][x - 5]

        print(right_top_area["longitude"], right_top_area["latitude"])
        print(left_top_area["longitude"], left_top_area["latitude"])
        print(left_bottom_area["longitude"], left_bottom_area["latitude"])
        print(right_bottom_area["longitude"], right_bottom_area["latitude"])

        polygon = []
        polygon.append([right_top_area["latitude"], right_top_area["longitude"]])
        polygon.append([left_top_area["latitude"], left_top_area["longitude"]])
        polygon.append([left_bottom_area["latitude"], left_bottom_area["longitude"]])
        polygon.append([right_bottom_area["latitude"], right_bottom_area["longitude"]])
        polygon.append([right_top_area["latitude"], right_top_area["longitude"]])

        return jsonify({"polygon": polygon})


@generate_route.route('/add_route', methods=['POST'])
def add_route():
    if request.method == "POST":
        ship_name = request.json["ship_name"]
        iceclass = request.json["iceclass"]

        start_longitude = request.json["start_longitude"]
        start_latitude = request.json["start_latitude"]

        end_longitude = request.json["end_longitude"]
        end_latitude = request.json["end_latitude"]

        area_building_route = request.json["area_building_route"]

        date_start = request.json["date_start"]

        route_name = request.json["route_name"]

        print(f"Корабль: {ship_name}")
        print(f"ледовый класс: {iceclass}")
        print(f"Начало: long {start_longitude}, lat {start_latitude}")
        print(f"Конец: long {end_longitude}, lat {end_latitude}")
        print(f"Область постройки маршрута: \n"
              f"левая вершина: long: {area_building_route[0][1]}, lat: {area_building_route[0][0]} \n"
              f"правая вершина: long: {area_building_route[1][1]}, lat: {area_building_route[1][0]} \n"
              f"правый низ: long: {area_building_route[2][1]}, lat: {area_building_route[2][0]} \n"
              f"левый низ: long: {area_building_route[3][1]}, lat: {area_building_route[3][0]} \n")

        print(f"Дата отправки: {date_start}")
        print(f"Название маршрута: {route_name}")

        with open("data/map.json", "r") as file:
            map_ = json.load(file)

        area = route_building_area.build_interval_route(map_, area_building_route)

        area_width = len(area)
        area_length = len(area[0])
        print(area_width)
        print(area_length)
        area_y_next_point, area_x_next_point = route_building_area.nearest(
            area,
            area_width,
            area_length,
            end_longitude,
            end_latitude
        )

        area_y_start_point, area_x_star_point = route_building_area.nearest(
            area,
            area_width,
            area_length,
            start_longitude,
            start_latitude
        )

        area[area_y_start_point][area_x_star_point]["start"] = True
        area[area_y_next_point][area_x_next_point]["end"] = True

        print(area_y_next_point, area_x_next_point)
        print(area_y_start_point, area_x_star_point)

        graph = create_graph.create(area, iceclass)
        src, dest = create_src_dest.create_src_dest(area)
        dijkstra.dijkstra(graph, src, dest)

        return "hello"




