from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from config import Config
import json


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)


from app import routes