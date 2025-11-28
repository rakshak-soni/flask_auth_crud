from base.com.dao.user_dao import UserDAO
from base.com.vo.user_vo import UserVO
from base.com.utils.hashing import hash_password
from base.com.utils.time_utils import current_time
from base.com.dao.user_role_dao import UserRoleDAO
from base.com.vo.user_role_vo import UserRoleVO
from base.com.dao.role_dao import RoleDAO

class RegisterService:

    @staticmethod
    def register_user(data):
        try:
            # Validate required fields
            required = ["first_name", "last_name", "user_email", "user_password", "user_phone"]
            for field in required:
                if field not in data or not data[field]:
                    return {"status": "error", "message": f"{field} is required"}, 400

            # Check email exists
            existing = UserDAO.get_user_by_email(data["user_email"])
            if existing:
                return {"status": "error", "message": "Email already registered"}, 409

            # Create new user
            user_vo = UserVO(
                first_name=data["first_name"],
                last_name=data["last_name"],
                user_email=data["user_email"],
                user_phone=data["user_phone"],
                user_password=hash_password(data["user_password"]),
                created_at=current_time(),
                updated_at=current_time(),
                user_is_verified=True
            )

            new_user = UserDAO.insert_user(user_vo)

            # Check user count to assign role
            total_users = UserDAO.count_users()  # You must implement this in DAO
            role_name = "admin" if total_users == 1 else "user"  # first user → admin

            # Fetch role
            role = RoleDAO.get_role_by_name(role_name)

            # Insert role assignment
            user_role_vo = UserRoleVO(
                user_role_user_id=new_user.user_id,
                user_role_role_id=role.role_id
            )
            UserRoleDAO.insert_user_role(user_role_vo)

            return (
                {"status": "success", "message": "Registration successful"},
                201,
            )

        except Exception as e:
            return {
                "status": "error",
                "message": "Internal server error",
                "details": str(e)   # remove in production
            }, 500
