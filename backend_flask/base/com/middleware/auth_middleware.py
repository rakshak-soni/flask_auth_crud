from functools import wraps
from flask import request, jsonify
from base.com.utils.auth_utils import decode_jwt

def token_required(required_roles=None):
    if required_roles is None:
        required_roles = []

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                # 1. Extract Authorization header
                auth_header = request.headers.get("Authorization", "")
                if not auth_header.startswith("Bearer "):
                    return jsonify({"error": "Token missing or malformed"}), 401

                token = auth_header.split("Bearer ")[-1].strip()
                if not token:
                    return jsonify({"error": "Token missing"}), 401

                # 2. Decode token
                payload = decode_jwt(token)
                if not payload:
                    return jsonify({"error": "Invalid or expired token"}), 401

                # 3. Extract roles and verify
                user_roles = payload.get("roles", [])
                if not isinstance(user_roles, list):
                    return jsonify({"error": "Invalid token roles format"}), 400

                if required_roles and not any(role in user_roles for role in required_roles):
                    return jsonify({"error": "Forbidden: insufficient privileges"}), 403

                # 4. Attach user info
                request.user_id = payload.get("user_id")
                request.user_roles = user_roles

                if request.user_id is None:
                    return jsonify({"error": "Malformed token: user_id missing"}), 400

                # 5. Call original function
                return fn(*args, **kwargs)

            except Exception as e:
                # Generic fallback to prevent internal errors leaking to client
                return jsonify({
                    "error": "Internal server error during authentication",
                    "details": str(e)
                }), 500

        return wrapper

    return decorator
