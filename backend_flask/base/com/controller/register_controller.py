from flask import request, jsonify
from base import app
from base.com.service.register_service import RegisterService
import traceback


@app.route("/register", methods=["POST"])
def rest_register():
    try:
        # Validate JSON request
        if not request.is_json:
            return jsonify({"status": "error", "message": "Request must be JSON"}), 400

        try:
            data = request.get_json()
        except Exception as json_err:
            print("JSON PARSE ERROR:", str(json_err))
            return jsonify({"status": "error", "message": "Invalid JSON format"}), 400

        try:
            result, status = RegisterService.register_user(data)
        except Exception as service_err:
            print("SERVICE ERROR register_user:", str(service_err))
            print(traceback.format_exc())
            return jsonify({"status": "error", "message": "Internal server error"}), 500

        return jsonify(result), status

    except Exception as e:
        print("UNEXPECTED ERROR:", str(e))
        print(traceback.format_exc())
        return jsonify({"status": "error", "message": "Internal server error"}), 500
