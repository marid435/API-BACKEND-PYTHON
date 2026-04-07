from flask import jsonify

from src.config.database import get_connection


def check_database() -> tuple:
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1 AS ok")
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        ok_value = result[0] if result else None
        return jsonify({"database": "connected", "ok": ok_value}), 200
    except Exception as error:
        return jsonify({"database": "disconnected", "error": str(error)}), 500
