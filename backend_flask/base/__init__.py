import warnings
from datetime import timedelta
import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # Load .env

warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

app = Flask(__name__)
CORS(app)

app.secret_key = os.getenv("FLASK_SECRET_KEY")

DB_HOST = os.getenv("DB_HOST")

app.config['SQLALCHEMY_ECHO'] = os.getenv("SQLALCHEMY_ECHO") == "True"
app.config['SQLALCHEMY_MAX_OVERFLOW'] = int(os.getenv("SQLALCHEMY_MAX_OVERFLOW"))

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(
    minutes=int(os.getenv("PERMANENT_SESSION_LIFETIME"))
)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
    f"@{DB_HOST}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
print("DB URI:", app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)
app.app_context().push()

migrate = Migrate(app, db)

from base.com import controller
