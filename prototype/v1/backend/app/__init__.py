from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


from app import routes