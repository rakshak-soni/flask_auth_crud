# dao/user_dao.py
from base import db
from base.com.vo.user_vo import UserVO

class UserDAO:

    @staticmethod
    def insert_user(user_vo):
        db.session.add(user_vo)
        db.session.commit()
        return user_vo

    @staticmethod
    def get_user_by_email(email):
        return UserVO.query.filter_by(user_email=email).first()
    
    @staticmethod
    def count_users():
        return UserVO.query.count()
