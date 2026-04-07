from flask import jsonify


def ping() -> tuple:
    return jsonify({"message": "pong"}), 200
