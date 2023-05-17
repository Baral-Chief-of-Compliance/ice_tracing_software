from app import Blueprint, jsonify, request, json
from app.use_db import route_inf_db
from app.tools import route_building_area
from app.tools import create_graph
from app.tools import create_src_dest
from app.tools import dijkstra
from app.use_db import generate_route_db


route_inf = Blueprint('route_inf', __name__)


@route_inf.route('/route_inf', methods=['GET'])
def show_routes():
    if request.method == "GET":
        id_per = 1
        routes_json = []
        routes = route_inf_db.show_routes(id_per)

        for route in routes:
            routes_json.append({
                'id_rt': route[0],
                'name': route[1],
                'name_sh': route[2],
                'ice_class': route[3]
            })

        return jsonify({
            'routes': routes_json
        })


@route_inf.route('/route_inf/<int:id_rt>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_int_route(id_rt):
    if request.method == "GET":

        json_points = []
        json_routes = []
        route_inf, \
            inf_about_start, \
            inf_about_end, \
            intermediates, \
            itirerarys, \
            final_point = route_inf_db.show_inf_about_route(1, id_rt)

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

        # print(f"name {route_inf[1]}")
        # print(f"ship_name: {route_inf[2]}")
        # print(f"ice_class {route_inf[3]}")
        # print(f"date_start {inf_about_start[2]}")
        # print(f"start_longitude: {float(inf_about_start[0])}")
        # print(f"start_latitude: {float(inf_about_start[1])}")
        # print(f"end_longitude: {float(inf_about_end[0])}")
        # print(f"end_latitude: {float(inf_about_end[1])}")
        # print(f"points: {json_points}")
        # print(f"routes: {json_routes}")
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
            "final_point_longitude": float(final_point[0]),
            "final_point_latitude": float(final_point[1])
        })

    elif request.method == 'PUT':
        date_enter = request.json["date_enter"]

        route_inf_db.set_data_on_point(1, id_rt, date_enter)
        return "date on point is update"

    elif request.method == 'POST':
        print("\n\nжукич лох\n\n")

        final_point_longitude = request.json["final_point_longitude"]
        final_point_latitude = request.json["final_point_latitude"]
        print(f"final_long_start: {final_point_longitude}" )
        print(f"final_lat_start: {final_point_latitude}")

        print(final_point_longitude)
        print(final_point_latitude)


        end_longitude = request.json["end_longitude"]
        end_latitude = request.json["end_latitude"]
        print(f"\n\nlong_end: {end_longitude}" )
        print(f"lat_end: {end_latitude}")

        iceclass = request.json["iceclass"]

        area_building_route = request.json["area_building_route"]

        with open("data/map.json", "r") as file:
            map_ = json.load(file)

        print("\n\n")
        print(area_building_route)
        print("\n\n")
        area = route_building_area.build_interval_route(map_, area_building_route)

        # with open("data/area_check.json", "w") as file:
        #     json.dump(area, file)

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

        print(f"\n\nLong_next_point: {area[area_y_next_point][area_x_next_point]['longitude']}")
        print(f"Lat_next_point: {area[area_y_next_point][area_x_next_point]['latitude']}")

        area_y_start_point, area_x_start_point = route_building_area.nearest(
            area,
            area_width,
            area_length,
            final_point_longitude,
            final_point_latitude
        )

        print(f"\n\nLong_start_point: {area[area_y_start_point][area_x_start_point]['longitude']}")
        print(f"Lat_start_point: {area[area_y_start_point][area_x_start_point]['latitude']}")

        area[area_y_start_point][area_x_start_point]["start"] = True
        area[area_y_next_point][area_x_next_point]["end"] = True

        generate_route_db.add_intermediate(
            id_rt,
            area[area_y_next_point][area_x_next_point]["longitude"],
            area[area_y_next_point][area_x_next_point]["latitude"]
        )

        print(area_y_next_point, area_x_next_point)
        print(area_y_start_point, area_x_start_point)

        graph = create_graph.create(area, iceclass)
        src, dest = create_src_dest.create_src_dest(area)
        print(f"src: {src}")
        print(f"dest: {dest}")
        dijkstra.dijkstra(graph, src, dest)

        with open("data/pathArc7.json", "r") as file:
            polyline_for_ymap = json.load(file)

        # with open("data/pathArc7.json", "w") as file:
        #     json.dump("", file)
        #
        # with open("data/pathArc7_map_box.json", "w") as file:
        #     json.dump("", file)

        json_way = json.dumps(polyline_for_ymap)

        generate_route_db.add_route(id_rt, json_way)
        return "hello"

    elif request.method == 'DELETE':

        route_inf_db.delete_route(id_rt)

        return jsonify(f"route {id_rt} is delete")

