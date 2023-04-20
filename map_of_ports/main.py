from flask import Flask, jsonify, redirect, url_for, request, render_template
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return redirect(url_for('ports_map'))


@app.route('/ports', methods=['GET'])
def all_ports():
    if request.method == 'GET':
        with open('./data/ports.json',  encoding="utf-8") as f:
            ports = json.load(f)

        return jsonify(ports)


@app.route('/ports_map', methods=['GET'])
def ports_map():
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
