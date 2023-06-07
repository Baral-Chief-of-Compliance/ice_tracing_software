from app import Blueprint, jsonify, request, json
from app.use_db import route_inf_db
from app.tools import route_building_area
from app.tools import create_graph
from app.tools import create_src_dest
from app.tools import dijkstra
from app.use_db import generate_route_db
from app.tools.convert_path_to_geojson import convert
from authorization.decorator_for_authorization import token_required
from app import redis_data_base
from ice.ice_object_border import clear
from ice.create_polygon import clean_map
from generate_ice_conditions.format_polygons import format_polygons
from generate_route.generate_route import create_geojson, CustomThread


route_inf = Blueprint('route_inf', __name__)


@route_inf.route('/route_inf', methods=['GET'])
@token_required
def show_routes(id_per):
    if request.method == "GET":
        routes_json = []
        routes = route_inf_db.show_routes(id_per)

        for route in routes:
            routes_json.append({
                'id_rt': route[0],
                'name': route[1],
                'name_sh': route[2],
                'ice_class': route[3],
                'status': route[4],
                'date_enter': route[5]
            })

        return jsonify({
            'routes': routes_json
        })


@route_inf.route('/route_inf/<int:id_rt>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@token_required
def get_int_route(id_per, id_rt):
    if request.method == "GET":

        json_points = []
        json_routes = []
        route_inf, inf_about_start, inf_about_end, intermediates, itirerarys, final_point \
            = route_inf_db.show_inf_about_route(id_per, id_rt)

        status = route_inf_db.get_status(id_rt)

        for point in intermediates:
            json_points.append({
                "point_longitude": point[0],
                "point_latitude": point[1],
                "date": point[2]
            })

        for route in itirerarys:
            json_routes.append({
                "polyline": json.loads(route[0])
            })

        if status == 'в процессе':

            return jsonify({
                "name": route_inf[1],
                "ship_name": route_inf[2],
                "ice_class": route_inf[3],
                "date_start": inf_about_start[2],
                "start_longitude": float(inf_about_start[0]),
                "start_latitude": float(inf_about_start[1]),
                "end_longitude": float(inf_about_end[0]),
                "end_latitude": float(inf_about_end[1]),
                "points": json_points,
                "routes": json_routes,
                "status": status,
                "final_point_longitude": float(final_point[0]),
                "final_point_latitude": float(final_point[1]),
                "date_end": "--"
            })

        elif status == 'завершение':

            return jsonify({
                "name": route_inf[1],
                "ship_name": route_inf[2],
                "ice_class": route_inf[3],
                "date_start": inf_about_start[2],
                "start_longitude": float(inf_about_start[0]),
                "start_latitude": float(inf_about_start[1]),
                "end_longitude": float(inf_about_end[0]),
                "end_latitude": float(inf_about_end[1]),
                "points": json_points,
                "routes": json_routes,
                "status": status,
                "date_end": "--"
            })

        else:
            date_end = route_inf_db.get_date_end(id_rt)
            return jsonify({
                "name": route_inf[1],
                "ship_name": route_inf[2],
                "ice_class": route_inf[3],
                "date_start": inf_about_start[2],
                "start_longitude": float(inf_about_start[0]),
                "start_latitude": float(inf_about_start[1]),
                "end_longitude": float(inf_about_end[0]),
                "end_latitude": float(inf_about_end[1]),
                "points": json_points,
                "routes": json_routes,
                "status": status,
                "date_end": date_end
            })

    elif request.method == 'POST':

        date_enter = request.json["date_enter"]

        route_inf_db.set_data_on_point(id_per, id_rt, date_enter)

        start_point_longitude = request.json["start_point_longitude"]
        start_point_latitude = request.json["start_point_latitude"]

        end_point_longitude = request.json["end_point_longitude"]
        end_point_latitude = request.json["end_point_latitude"]

        final_point_longitude = request.json["final_point_longitude"]
        final_point_latitude = request.json["final_point_latitude"]

        iceclass = request.json["iceclass"]

        area_building_route = request.json["area_building_route"]

        if redis_data_base.get(id_per):
            map_ = json.loads(redis_data_base.get(id_per))

        else:
            with open("data/map_test.json", "r") as file:
                map_ = json.load(file)

        area = route_building_area.build_interval_route(map_, area_building_route)

        # with open("data/area_check.json", "w") as file:
        #     json.dump(area, file)

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

        final_point_longitude = area[area_y_next_point][area_x_next_point]["longitude"]
        final_point_latitude = area[area_y_next_point][area_x_next_point]["latitude"]

        if final_point_latitude == end_point_latitude and final_point_longitude == end_point_longitude:
            route_inf_db.update_status_completion(id_rt)

        else:

            generate_route_db.add_intermediate(
                id_rt,
                area[area_y_next_point][area_x_next_point]["longitude"],
                area[area_y_next_point][area_x_next_point]["latitude"]
            )
    
        graph = create_graph.create(area, iceclass)

        start, goal = create_src_dest.create_src_dest(area)

        path = dijkstra.dijkstra(graph, start, goal)

        polyline_for_ymap = convert(path)

        json_way = json.dumps(polyline_for_ymap)

        max_id_itirerary = generate_route_db.add_route(id_rt, json_way)

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

        return jsonify("path is build")

    elif request.method == 'DELETE':

        route_inf_db.delete_route(id_rt)

        return jsonify(f"route {id_rt} is delete")

    elif request.method == 'PUT':
        date_enter = request.json["date_enter"]

        route_inf_db.update_status(id_rt, date_enter)

        return jsonify(f"status route is update")


