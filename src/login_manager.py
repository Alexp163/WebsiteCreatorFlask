from flask_login import LoginManager
from app import app
from models import User


login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
