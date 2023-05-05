from app import Blueprint, jsonify, request, json


ports = Blueprint('ports', __name__)


@ports.route('/ports', methods=['GET'])
def show_ports():
    if request.method == "GET":
        ports = []
        with open("ports/all_ports.json", "r") as file:
            ports = json.load(file)

        return jsonify(
            {
                "ports": ports
            }
        )
