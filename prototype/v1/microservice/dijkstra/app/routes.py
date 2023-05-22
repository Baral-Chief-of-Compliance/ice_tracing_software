from app import app, Blueprint
from build_route.build_route import build_route
import os


@app.route('/')
def hello():
    return "hello"


app.register_blueprint(build_route, url_prefix='/iceocean/api/v1.0/microservice/')
