from app import app, request, Blueprint
from generate_route.generate_route import generate_route


@app.route('/')
def index():
    return "hello world"


app.register_blueprint(generate_route, url_prefix='/iceocean/api/v1.0/')
