from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from config import Config
import json
from flask_mysqldb import MySQL
import MySQLdb.cursors
import redis


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mysql = MySQL(app)
redis_data_base = redis.Redis(host='localhost', port=6379, db=1)


from app import routes