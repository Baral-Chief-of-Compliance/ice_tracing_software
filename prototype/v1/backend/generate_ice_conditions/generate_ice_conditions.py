from app import Blueprint, jsonify, request, json


generate_ice_conditions = Blueprint('generate_ice_conditions', __name__)


@generate_ice_conditions.route('/today/young_ice', methods=['GET'])
def today_young_ice():
    if request.method == "GET":
        with open("ice/json/young_ice.json") as file:
            young_ice = json.load(file)

        young_ice_polygons = []
        for ice in young_ice["features"]:
            polygon = []

            for el in ice["geometry"]["coordinates"][0]:
                long, lat = el[0], el[1]
                polygon.append([lat, long])
            young_ice_polygons.append(polygon)

        return jsonify({"polygons": young_ice_polygons})

