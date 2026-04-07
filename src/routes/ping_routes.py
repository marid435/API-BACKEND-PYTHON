from flask import Blueprint

from src.controllers.ping_controller import ping

ping_blueprint = Blueprint("ping", __name__)

ping_blueprint.route("/ping", methods=["GET"])(ping)
