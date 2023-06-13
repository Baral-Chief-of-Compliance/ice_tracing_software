from app import Blueprint, jsonify, request, json
from generate_ice_conditions.format_polygons import format_polygons
from authorization.decorator_for_authorization import token_required
from ice import test_form_jupyter
from app.use_db import generate_ice_conditions_db
import sys
from threading import Thread
from ice.ice_object_border import clear
from ice.create_polygon import clean_map
from app import redis_data_base
from PIL import Image
import numpy as np
from ice.create_ice_from_photo import create_ice_from_photo


generate_ice_conditions = Blueprint('generate_ice_conditions', __name__)


@generate_ice_conditions.route('/today/young_ice', methods=['GET'])
@token_required
def today_young_ice(id_per):
    if request.method == "GET":
        with open("ice/json/young_ice.json") as file:
            young_ice = json.load(file)

        young_ice_polygons = format_polygons(young_ice)

        return jsonify({"polygons": young_ice_polygons})


@generate_ice_conditions.route('/today/first_year_ice', methods=['GET'])
@token_required
def today_first_year_ice(id_per):
    if request.method == "GET":
        with open("ice/json/first_year_ice.json") as file:
            first_year_ice = json.load(file)

        first_year_ice_polygons = format_polygons(first_year_ice)

        return jsonify({"polygons": first_year_ice_polygons})


@generate_ice_conditions.route('/today/old_ice', methods=['GET'])
@token_required
def today_old_ice(id_per):
    if request.method == 'GET':
        with open("ice/json/old_ice.json") as file:
            old_ice = json.load(file)

        old_ice_polygons = format_polygons(old_ice)

        return jsonify({"polygons": old_ice_polygons})


@generate_ice_conditions.route('/today/fast_ice', methods=['GET'])
@token_required
def today_fast_ice(id_per):
    if request.method == 'GET':
        with open("ice/json/fast_ice.json") as file:
            fast_ice = json.load(file)

        fast_ice_polygons = format_polygons(fast_ice)

        return jsonify({"polygons": fast_ice_polygons})


@generate_ice_conditions.route('/today/ice_field', methods=['GET'])
@token_required
def today_ice_field(id_per):
    if request.method == 'GET':
        with open("ice/json/ice_field.json") as file:
            ice_field = json.load(file)

        ice_field_polygons = format_polygons(ice_field)

        return jsonify({"polygons": ice_field_polygons})


@generate_ice_conditions.route('/today/nilas_ice', methods=['GET'])
@token_required
def today_nilas_ice(id_per):
    if request.method == 'GET':
        with open("ice/json/nilas_ice.json") as file:
            nilas_ice = json.load(file)

        nilas_ice_polygons = format_polygons(nilas_ice)

        return jsonify({"polygons": nilas_ice_polygons})


class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return


def create_geojson(map_, type_of_ice):
    map_ = clear(map_, type_of_ice)
    geojson = clean_map(map_, type_of_ice)

    ice_field_geojson = format_polygons(geojson)
    return ice_field_geojson


def add_data_to_redis(map_, id_per):
    json_map = json.dumps(map_)
    redis_data_base.set(id_per, json_map)
    print(f"map into redis for person {id_per}")


@generate_ice_conditions.route('/random/ice_conditions', methods=['GET'])
@token_required
def random_ice_conditions(id_per):
    if request.method == 'GET':
        sys.setrecursionlimit(5000)

        map_ = generate_ice_conditions_db.get_map()

        map_ = test_form_jupyter.create_ice(map_)

        redis_thread = Thread(target=add_data_to_redis, args=(map_, id_per))
        t1 = CustomThread(target=create_geojson, args=(map_, "first_year_ice"))
        t2 = CustomThread(target=create_geojson, args=(map_, "young_ice"))
        t3 = CustomThread(target=create_geojson, args=(map_, "old_ice"))
        t4 = CustomThread(target=create_geojson, args=(map_, "nilas_ice"))
        t5 = CustomThread(target=create_geojson, args=(map_, "fast_ice"))
        t6 = CustomThread(target=create_geojson, args=(map_, "ice_field"))

        redis_thread.start()

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

        redis_thread.join()

        first_year_ice = t1.join()
        young_ice = t2.join()
        old_ice = t3.join()
        nilas_ice = t4.join()
        fast_ice = t5.join()
        ice_field = t6.join()



        return jsonify({
            "first_year_ice": first_year_ice,
            "young_ice": young_ice,
            "old_ice": old_ice,
            "nilas_ice": nilas_ice,
            "fast_ice": fast_ice,
            "ice_field": ice_field
        })


@generate_ice_conditions.route('/download_photo/ice_conditions', methods=['POST'])
@token_required
def ice_conditions_from_photo(id_per):
    if request.method == 'POST':
        sys.setrecursionlimit(5000)
        photo_ice_condition = request.files['image']

        img = np.asarray(Image.open(photo_ice_condition).convert('RGB'))

        map_ = generate_ice_conditions_db.get_map()

        map_ = create_ice_from_photo(img, map_)

        redis_thread = Thread(target=add_data_to_redis, args=(map_, id_per))
        t1 = CustomThread(target=create_geojson, args=(map_, "first_year_ice"))
        t2 = CustomThread(target=create_geojson, args=(map_, "young_ice"))
        t3 = CustomThread(target=create_geojson, args=(map_, "old_ice"))
        t4 = CustomThread(target=create_geojson, args=(map_, "nilas_ice"))
        t5 = CustomThread(target=create_geojson, args=(map_, "fast_ice"))
        t6 = CustomThread(target=create_geojson, args=(map_, "ice_field"))

        redis_thread.start()

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

        redis_thread.join()

        first_year_ice = t1.join()
        young_ice = t2.join()
        old_ice = t3.join()
        nilas_ice = t4.join()
        fast_ice = t5.join()
        ice_field = t6.join()

        return jsonify({
            "first_year_ice": first_year_ice,
            "young_ice": young_ice,
            "old_ice": old_ice,
            "nilas_ice": nilas_ice,
            "fast_ice": fast_ice,
            "ice_field": ice_field
        })


@generate_ice_conditions.route('/download_geojson/ice_conditions', methods=['POST'])
@token_required
def ice_conditions_from_geojson(id_per):
    if request.method == 'POST':
        sys.setrecursionlimit(5000)
        first_year_ice_file = request.files['first_year_ice']
        young_ice_file = request.files['young_ice']
        old_ice_file = request.files['old_ice']
        nilas_ice_file = request.files['nilas_ice']
        fast_ice_file = request.files['fast_ice']
        ice_field_file = request.files['ice_field']

        first_year_ice_json = json.load(first_year_ice_file)
        young_ice_json = json.load(young_ice_file)
        old_ice_json = json.load(old_ice_file)
        nilas_ice_json = json.load(nilas_ice_file)
        fast_ice_json = json.load(fast_ice_file)
        ice_field_json = json.load(ice_field_file)

        first_year_ice = format_polygons(first_year_ice_json)
        young_ice = format_polygons(young_ice_json)
        old_ice = format_polygons(old_ice_json)
        nilas_ice = format_polygons(nilas_ice_json)
        fast_ice = format_polygons(fast_ice_json)
        ice_field = format_polygons(ice_field_json)

        return jsonify({
            "first_year_ice": first_year_ice,
            "young_ice": young_ice,
            "old_ice": old_ice,
            "nilas_ice": nilas_ice,
            "fast_ice": fast_ice,
            "ice_field": ice_field
        })
