from base import db

class UserVO(db.Model):
    __tablename__ = 'user'

    user_id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column("first_name", db.String(255), nullable=False)
    last_name = db.Column("last_name", db.String(255), nullable=False)
    user_email = db.Column("user_email", db.String(255), nullable=False, unique=True)
    user_password = db.Column("user_password", db.String(255), nullable=False)
    user_is_verified = db.Column("user_is_verified", db.Boolean, default=False)
    user_phone = db.Column("user_phone", db.String(20))
    created_at = db.Column("created_at", db.DateTime)
    updated_at = db.Column("updated_at", db.DateTime)

    def as_dict(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'user_email': self.user_email,
            'user_password': self.user_password,
            'user_is_verified': self.user_is_verified,
            'user_phone': self.user_phone,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
        }


