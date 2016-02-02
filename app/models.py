from app import db
import datetime

from flask import g
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    id            = db.Column(db.Integer, primary_key = True)
    username      = db.Column('username', db.String(20), unique=True, index=True)
    email         = db.Column('email', db.String(120), index=True, unique=True)
    notes         = db.relationship('Notebook', backref='username', lazy='dynamic')
    todo          = db.relationship('Todo')
    pw_hash       = db.Column('password', db.String())
    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email    = email
    
    def is_active(self):
        """All user will be active"""
        return True
    
    
    def get_id(self):
        return str(self.id)
        
    def is_authenticated(self):
        """Return True if the user is authenticated"""
        return True
        
    def is_anonymous(self):
        return False
        
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
        
    def __repr__(self):
        return '<User %r>' % (self.username)
    
        
class Notebook(db.Model):
    id       = db.Column(db.Integer, primary_key = True)
    name     = db.Column(db.String())
    notes    = db.relationship('Note')
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, user_id, name):
        self.name    = name
        self.user_id = user_id
        
        
            
class Note(db.Model):
    id           = db.Column(db.Integer, primary_key = True)
    title        = db.Column(db.String())
    key_point    = db.Column(db.String())
    notes        = db.Column(db.String())
    summary      = db.Column(db.String())
    date_added   = db.Column(db.Date, default=datetime.date.today())
    course_id    = db.Column(db.Integer, db.ForeignKey('notebook.id'))
    user_id      = db.Column(db.Integer)
    
    def __init__(self, title, key_point, notes, summary, course_id, user_id):
        self.title     = title
        self.key_point = key_point
        self.notes     = notes
        self.summary   = summary
        self.course_id = course_id
        self.user_id   = user_id
    def __repr__(self):
        return '<Note %r>' % (self.title)


class Todo(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    title       = db.Column(db.String())
    description = db.Column(db.String())
    date_due    = db.Column(db.Date)
    is_done     = db.Column(db.Boolean, unique=False, default=False)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, title, description, date_due, user_id):
        self.title       = title
        self.description = description
        self.date_due    = date_due
        self.user_id     = user_id


