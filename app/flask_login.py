import flask.ext.login as flask_login
from app import app

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def user_loader(username):
    User.get(User.username == username)
    