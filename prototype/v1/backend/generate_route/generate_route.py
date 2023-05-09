from app import Blueprint, jsonify, request, json
from app.tools import route_building_area


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



