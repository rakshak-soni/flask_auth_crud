from base import db
from base.com.vo.user_role_vo import UserRoleVO

class UserRoleDAO:

    @staticmethod
    def insert_user_role(user_role_vo):
        db.session.add(user_role_vo)
        db.session.commit()
