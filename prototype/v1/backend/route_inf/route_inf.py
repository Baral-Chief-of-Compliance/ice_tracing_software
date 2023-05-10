from app import Blueprint, jsonify, request, json
from app.use_db import route_inf_db


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


@route_inf.route('/route_inf/<int:id_rt>', methods=['GET', 'POST'])
def get_int_route(id_rt):
    if request.method == "GET":

        json_points = []
        json_routes = []
        route_inf, inf_about_start, inf_about_end, intermediates, itirerarys = route_inf_db.show_inf_about_route(1, id_rt)

        for point in intermediates:
            json_points.append({
                "point_longitude": point[0],
                "point_latitude": point[1]
            })

        for route in itirerarys:
            json_routes.append({
                "polyline": route[0]
            })

        print(f"name {route_inf[1]}")
        print(f"ship_name: {route_inf[2]}")
        print(f"ice_class {route_inf[3]}")
        print(f"start_longitude: {inf_about_start[0]}")
        print(f"start_latitude: {inf_about_start[1]}")
        print(f"end_longitude: {inf_about_end[0]}")
        print(f"end_latitude: {inf_about_end[1]}")
        print(f"points: {json_points}")
        print(f"routes: {json_routes}")
        return jsonify({
            "name": route_inf[1],
            "ship_name": route_inf[2],
            "ice_class": route_inf[3],
            "start_longitude": inf_about_start[0],
            "start_latitude": inf_about_start[1],
            "end_longitude": inf_about_end[0],
            "end_latitude": inf_about_end[1],
            "points": json_points,
            "routes": json_routes
        })