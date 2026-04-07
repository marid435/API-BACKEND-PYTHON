from flask import Flask

from src.routes.db_routes import db_blueprint
from src.routes.ping_routes import ping_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(ping_blueprint)
    app.register_blueprint(db_blueprint)
    return app
