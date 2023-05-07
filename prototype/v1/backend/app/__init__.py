from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from config import Config
import json
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mysql = MySQL(app)


from app import routes