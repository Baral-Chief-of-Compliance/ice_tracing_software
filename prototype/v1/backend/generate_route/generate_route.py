from app import Blueprint, jsonify, request, json
from app.tools import route_building_area
from app.tools import create_graph
from app.tools import create_src_dest
from app.tools import dijkstra
from app.use_db import generate_route_db
from app.tools.convert_path_to_geojson import convert
from authorization.decorator_for_authorization import token_required
from generate_route.define_status import check
from app import redis_data_base
from ice.ice_object_border import clear
from ice.create_polygon import clean_map
from generate_ice_conditions.format_polygons import format_polygons
from threading import Thread


generate_route = Blueprint('generate_route', __name__)


def create_geojson(map_, type_of_ice):
    map_ = clear(map_, type_of_ice)
    geojson = clean_map(map_, type_of_ice)

    ice_field_geojson = format_polygons(geojson)
    ice_field_geojson_dumps = json.dumps(ice_field_geojson)

    return ice_field_geojson_dumps


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


@generate_route.route('/generate_route', methods=['POST'])
@token_required
def generate(id_per):
    if request.method == 'POST':
        iceclass = request.json['iceclass']

        start_longitude = request.json['start_longitude']
        start_latitude = request.json['start_latitude']

        end_longitude = request.json['end_longitude']
        end_latitude = request.json['end_latitude']

        return jsonify({
            "iceclass": iceclass,
            "start_longitude": start_longitude,
            "start_latitude": start_latitude,
            "end_longitude": end_longitude,
            "end_latitude": end_latitude
        })


@generate_route.route('/generate_area', methods=['POST'])
@token_required
def define_square_area(id_per):
    if request.method == "POST":
        start_longitude = request.json["start_longitude"]
        start_latitude = request.json["start_latitude"]

        #проверяем вместо map.json map_test.json но в идеале заменить на подгрузку из бд
        with open("data/map_test.json", "r") as file:
            map_ = json.load(file)

        width = len(map_)
        length = len(map_[0])

        y, x = route_building_area.nearest(map_, width, length, start_longitude, start_latitude)

        right_top_area = map_[y - 2][x - 5]
        left_top_area = map_[y - 2][x + 5]
        left_bottom_area = map_[y + 2][x + 5]
        right_bottom_area = map_[y + 2][x - 5]

        polygon = []
        polygon.append([right_top_area["latitude"], right_top_area["longitude"]])
        polygon.append([left_top_area["latitude"], left_top_area["longitude"]])
        polygon.append([left_bottom_area["latitude"], left_bottom_area["longitude"]])
        polygon.append([right_bottom_area["latitude"], right_bottom_area["longitude"]])
        polygon.append([right_top_area["latitude"], right_top_area["longitude"]])

        return jsonify({"polygon": polygon})


@generate_route.route('/add_route', methods=['POST'])
@token_required
def add_route(id_per):
    if request.method == "POST":
        ship_name = request.json["ship_name"]
        iceclass = request.json["iceclass"]

        start_longitude = request.json["start_longitude"]
        start_latitude = request.json["start_latitude"]

        end_longitude = request.json["end_longitude"]
        end_latitude = request.json["end_latitude"]

        if redis_data_base.get(id_per):
            map_ = json.loads(redis_data_base.get(id_per))

        else:

            with open("data/map_test.json", "r") as file:
                map_ = json.load(file)

        nearest_start_y, nearest_start_x = route_building_area.nearest(
            map_,
            len(map_),
            len(map_[0]),
            start_longitude,
            start_latitude
        )

        nearest_end_y, nearest_end_x = route_building_area.nearest(
            map_,
            len(map_),
            len(map_[0]),
            end_longitude,
            end_latitude
        )

        start_longitude = map_[nearest_start_y][nearest_start_x]["longitude"]
        start_latitude = map_[nearest_start_y][nearest_start_x]["latitude"]

        end_longitude = map_[nearest_end_y][nearest_end_x]["longitude"]
        end_latitude = map_[nearest_end_y][nearest_end_x]["latitude"]

        area_building_route = request.json["area_building_route"]

        date_start = request.json["date_start"]

        route_name = request.json["route_name"]

        # проверяем вместо map.json map_test.json но в идеале заменить на подгрузку из бд
        # with open("data/map_test.json", "r") as file:
        #     map_ = json.load(file)

        area = route_building_area.build_interval_route(map_, area_building_route)
        # print(area)
        area_width = len(area)
        area_length = len(area[0])

        area_y_next_point, area_x_next_point = route_building_area.nearest(
            area,
            area_width,
            area_length,
            end_longitude,
            end_latitude
        )

        area_y_start_point, area_x_start_point = route_building_area.nearest(
            area,
            area_width,
            area_length,
            start_longitude,
            start_latitude
        )

        area[area_y_start_point][area_x_start_point]["start"] = True
        area[area_y_next_point][area_x_next_point]["end"] = True

        id_sh = generate_route_db.add_ship(ship_name, iceclass)

        status_rt = check(area, end_longitude, end_latitude)

        id_rt = generate_route_db.create_route(route_name, id_per, id_sh, status_rt)

        generate_route_db.create_start_end_point(
            id_rt,
            start_longitude,
            start_latitude,
            end_longitude,
            end_latitude,
            date_start
        )

        if status_rt == 'в процессе':
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

        max_id_itirerary = generate_route_db.add_route(id_rt, json_path)

        t1 = CustomThread(target=create_geojson, args=(map_, "first_year_ice"))
        t2 = CustomThread(target=create_geojson, args=(map_, "young_ice"))
        t3 = CustomThread(target=create_geojson, args=(map_, "old_ice"))
        t4 = CustomThread(target=create_geojson, args=(map_, "nilas_ice"))
        t5 = CustomThread(target=create_geojson, args=(map_, "fast_ice"))
        t6 = CustomThread(target=create_geojson, args=(map_, "ice_field"))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

        first_year_ice = t1.join()
        young_ice = t2.join()
        old_ice = t3.join()
        nilas_ice = t4.join()
        fast_ice = t5.join()
        ice_field = t6.join()

        generate_route_db.add_ice_condition(max_id_itirerary, first_year_ice, "first_year_ice")
        generate_route_db.add_ice_condition(max_id_itirerary, young_ice, "young_ice")
        generate_route_db.add_ice_condition(max_id_itirerary, old_ice, "old_ice")
        generate_route_db.add_ice_condition(max_id_itirerary, nilas_ice, "nilas_ice")
        generate_route_db.add_ice_condition(max_id_itirerary, fast_ice, "fast_ice")
        generate_route_db.add_ice_condition(max_id_itirerary, ice_field, "ice_field")

        if redis_data_base.get(id_per):
            redis_data_base.delete(id_per)

        return jsonify("path is generate")


@generate_route.route('/get_coords_for_start_and_end', methods=['POST'])
@token_required
def get_coords_for_start_and_end(id_per):
    latitude = request.json["latitude"]
    longitude = request.json["longitude"]
    print(latitude)
    print(longitude)

    return jsonify({
        "latitude": float(latitude),
        "longitude": float(longitude)
    })




