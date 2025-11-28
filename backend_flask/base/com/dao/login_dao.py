# backend/base/com/dao/login_dao.py
from base import db
from base.com.vo.user_vo import UserVO
from base.com.vo.user_role_vo import UserRoleVO
from base.com.vo.role_vo import RoleVO
from base.com.vo.login_logs_vo import LoginLogsVO

class LoginDAO:

    @staticmethod
    def get_user_by_email(email):
        return UserVO.query.filter_by(user_email=email).first()

    @staticmethod
    def get_roles_by_user_id(user_id):
        user_roles = UserRoleVO.query.filter_by(user_role_user_id=user_id).all()
        roles = []
        for ur in user_roles:
            role = RoleVO.query.filter_by(role_id=ur.user_role_role_id).first()
            if role:
                roles.append(role.role_name)
        return roles

    @staticmethod
    def insert_login_log(user_id, username_attempt, status, ip_address, user_agent):
        log = LoginLogsVO(
            login_logs_user_id=user_id,
            username_attempt=username_attempt,
            status=status,
            ip_address=ip_address,
            user_agent=user_agent
        )
        db.session.add(log)
        db.session.commit()
