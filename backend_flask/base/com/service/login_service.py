# backend/base/com/service/login_service.py

from base.com.dao.login_dao import LoginDAO
from base.com.utils.auth_utils import generate_jwt
from base.com.utils.hashing import verify_password

class LoginService:

    @staticmethod
    def login_user(data, request):
        try:
            email = data.get("user_email")
            password = data.get("user_password")

            if not email or not password:
                return {"status": "error", "message": "Email and password are required"}, 400

            user = LoginDAO.get_user_by_email(email)

            # Invalid email
            if not user:
                LoginDAO.insert_login_log(
                    None,
                    email,
                    "FAILED",
                    request.remote_addr,
                    request.headers.get("User-Agent")
                )
                return {"status": "error", "message": "Invalid email or password"}, 401

            # Invalid password
            if not verify_password(password, user.user_password):
                LoginDAO.insert_login_log(
                    user.user_id,
                    email,
                    "FAILED",
                    request.remote_addr,
                    request.headers.get("User-Agent")
                )
                return {"status": "error", "message": "Invalid email or password"}, 401

            # Fetch roles
            roles = LoginDAO.get_roles_by_user_id(user.user_id)

            # Create token
            token = generate_jwt(user.user_id, roles)

            # Successful login log
            LoginDAO.insert_login_log(
                user.user_id,
                email,
                "SUCCESS",
                request.remote_addr,
                request.headers.get("User-Agent")
            )

            return {
                "status": "success",
                "token": token,
                "user": user.as_dict(),
                "roles": roles
            }, 200

        except Exception as e:
            # Unified fallback for any unexpected server-side error
            return {
                "status": "error",
                "message": "Internal server error",
                "details": str(e)    # remove in production for security
            }, 500
