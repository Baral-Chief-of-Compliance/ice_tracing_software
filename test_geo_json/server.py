from flask import Flask, request, jsonify
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        with open("../handel_photo_of_ice/geo_json_young_ice.json", "r") as file:
            geo_json = json.load(file)
        return jsonify(geo_json)


if __name__ == '__main__':
    app.run(debug=True)