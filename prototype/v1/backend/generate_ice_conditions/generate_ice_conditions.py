from app import Blueprint, jsonify, request, json
from generate_ice_conditions.format_polygons import format_polygons


generate_ice_conditions = Blueprint('generate_ice_conditions', __name__)


@generate_ice_conditions.route('/today/young_ice', methods=['GET'])
def today_young_ice():
    if request.method == "GET":
        with open("ice/json/young_ice.json") as file:
            young_ice = json.load(file)

        young_ice_polygons = format_polygons(young_ice)

        return jsonify({"polygons": young_ice_polygons})


@generate_ice_conditions.route('/today/first_year_ice', methods=['GET'])
def today_first_year_ice():
    if request.method == "GET":
        with open("ice/json/first_year_ice.json") as file:
            first_year_ice = json.load(file)

        first_year_ice_polygons = format_polygons(first_year_ice)

        return jsonify({"polygons": first_year_ice_polygons})


@generate_ice_conditions.route('/today/old_ice', methods=['GET'])
def today_old_ice():
    if request.method == 'GET':
        with open("ice/json/old_ice.json") as file:
            old_ice = json.load(file)

        old_ice_polygons = format_polygons(old_ice)

        return jsonify({"polygons": old_ice_polygons})


@generate_ice_conditions.route('/today/fast_ice', methods=['GET'])
def today_fast_ice():
    if request.method == 'GET':
        with open("ice/json/fast_ice.json") as file:
            fast_ice = json.load(file)

        fast_ice_polygons = format_polygons(fast_ice)

        return jsonify({"polygons": fast_ice_polygons})


@generate_ice_conditions.route('/today/ice_field', methods=['GET'])
def today_ice_field():
    if request.method == 'GET':
        with open("ice/json/ice_field.json") as file:
            ice_field = json.load(file)

        ice_field_polygons = format_polygons(ice_field)

        return jsonify({"polygons": ice_field_polygons})


@generate_ice_conditions.route('/today/nilas_ice', methods=['GET'])
def today_nilas_ice():
    if request.method == 'GET':
        with open("ice/json/nilas_ice.json") as file:
            nilas_ice = json.load(file)

        nilas_ice_polygons = format_polygons(nilas_ice)

        return jsonify({"polygons": nilas_ice_polygons})
