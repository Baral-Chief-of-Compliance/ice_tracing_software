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
