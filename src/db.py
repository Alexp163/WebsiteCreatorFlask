from flask_sqlalchemy import SQLAlchemy
from app import app


app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///slite.db"
db = SQLAlchemy(app)
