from app import app, request, Blueprint
from generate_route.generate_route import generate_route
from generate_ice_conditions.generate_ice_conditions import generate_ice_conditions
from ports.ports import ports
from route_inf.route_inf import route_inf
from authorization.authorization import authorization_blueprint
from app.use_db.enter_map_in_bd import add_map_to_bd
from authorization.decorator_for_authorization import token_required


url = '/iceocean/api/v1.0/'


@app.route('/')
@token_required
def index(id_per):
    return "hello world"


@app.route('/create_map')
def create_map():
    add_map_to_bd()
    return "map add to bd"


app.register_blueprint(generate_route, url_prefix=url)
app.register_blueprint(generate_ice_conditions, url_prefix=url)
app.register_blueprint(ports, url_prefix=url)
app.register_blueprint(route_inf, url_prefix=url)
app.register_blueprint(authorization_blueprint, url_prefix=url)
