import os
from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import login_user, logout_user, current_user, login_required, LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager. init_app(app)
    
from app import index
from app import register
from app import login_logout
from app import  new_note
from app import all_notes
from app import note
from app import edit_note
from app import delete
login_manager.login_view = 'login'
#from app import flask_log_in
@login_manager.user_loader
def load_user(email):
    return models.User.query.get(email)



