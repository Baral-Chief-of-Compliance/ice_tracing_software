from app import app, request, Blueprint
from generate_route.generate_route import generate_route
from generate_ice_conditions.generate_ice_conditions import generate_ice_conditions
from ports.ports import ports


@app.route('/')
def index():
    return "hello world"





app.register_blueprint(generate_route, url_prefix='/iceocean/api/v1.0/')
app.register_blueprint(generate_ice_conditions, url_prefix='/iceocean/api/v1.0/')
app.register_blueprint(ports, url_prefix='/iceocean/api/v1.0/')