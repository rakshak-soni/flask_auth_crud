# base/com/controller/login_controller.py
from flask import request, jsonify
from base import app
from base.com.service.login_service import LoginService
import traceback


@app.route("/login", methods=["POST"])
def login():
    try:
        # Validate JSON structure
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid or empty JSON payload"}), 400

        try:
            # Original logic (untouched)
            result, status_code = LoginService.login_user(data, request)
        except Exception as service_error:
            print("Service Error in login:", str(service_error))
            print(traceback.format_exc())
            return jsonify({"error": "Internal authentication error"}), 500

        return jsonify(result), status_code

    except Exception as e:
        # Unexpected failure handling
        print("Unexpected Error in login:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": "Internal server error"}), 500
