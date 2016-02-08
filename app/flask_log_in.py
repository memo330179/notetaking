import flask.ext.login as flask_login
from flask.ext.sqlalchemy import SQLAlchemy
from app import app, db, models

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def user_loader(user_id):
    return models.User.query.get(user_id)
    
