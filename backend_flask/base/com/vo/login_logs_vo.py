
from base import db

class LoginLogsVO(db.Model):
    __tablename__ = 'login_logs'

    login_logs_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # References login_users table (can be NULL for failed login)
    login_logs_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),
                                   nullable=True)

    # Stores attempted username even if failed
    username_attempt = db.Column(db.String(100), nullable=True)

    # SUCCESS / FAILED
    status = db.Column(db.Enum('SUCCESS', 'FAILED'), nullable=False)

    # Metadata
    ip_address = db.Column(db.String(50), nullable=True)
    user_agent = db.Column(db.Text, nullable=True)

    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=db.func.now())

    def as_dict(self):
        return {
            "login_logs_id": self.login_logs_id,
            "login_logs_user_id": self.login_logs_user_id,
            "username_attempt": self.username_attempt,
            "status": self.status,
            "ip_address": self.ip_address,
            "user_agent": self.user_agent,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S") if self.timestamp else None
        }

