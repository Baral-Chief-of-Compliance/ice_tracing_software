from app import Blueprint, jsonify, request


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
