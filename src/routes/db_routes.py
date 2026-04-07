from flask import Blueprint

from src.controllers.db_controller import check_database

db_blueprint = Blueprint("db", __name__)

db_blueprint.route("/health/db", methods=["GET"])(check_database)
