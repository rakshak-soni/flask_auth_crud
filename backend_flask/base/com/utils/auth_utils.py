import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_secret")
JWT_EXPIRY_HOURS = int(os.getenv("JWT_EXPIRY_HOURS", 2))
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

def generate_jwt(user_id, roles):
    try:
        payload = {
            "user_id": user_id,
            "roles": roles,
            "exp": datetime.utcnow() + timedelta(hours=JWT_EXPIRY_HOURS)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token

    except Exception:
        return None


def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload

    except jwt.ExpiredSignatureError:
        return {"error": "expired"}

    except jwt.InvalidTokenError:
        return {"error": "invalid"}

    except Exception as e:
        return {"error": str(e)}
