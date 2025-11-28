from base import db

class RoleVO(db.Model):
    __tablename__ = 'role'

    role_id = db.Column("role_id", db.Integer, primary_key=True, autoincrement=True, nullable=False)
    role_name = db.Column("role_name", db.String(255), nullable=False, unique=True)

    def as_dict(self):
        return {
            'role_id': self.role_id,
            'role_name': self.role_name
        }


