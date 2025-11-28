from base import db

class UserRoleVO(db.Model):
    __tablename__ = 'user_role'

    user_role_id = db.Column("user_role_id", db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_role_user_id = db.Column("user_id", db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user_role_role_id = db.Column("role_id", db.Integer, db.ForeignKey('role.role_id'), nullable=False)

    def as_dict(self):
        return {
            'user_role_id': self.user_role_id,
            'user_role_user_id': self.user_role_user_id,
            'user_role_role_id': self.user_role_role_id
        }


