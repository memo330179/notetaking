from app import db
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    id            = db.Column(db.Integer, primary_key = True)
    username      = db.Column('username', db.String(20), unique=True, index=True)
    email         = db.Column('email', db.String(120), index=True, unique=True)
    notes         = db.relationship('Note', backref='username', lazy='dynamic')
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
    
        
    
        
        
            
class Note(db.Model):
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))
    id        = db.Column(db.Integer, primary_key = True)
    title     = db.Column(db.String())
    course    = db.Column(db.String())
    key_point = db.Column(db.String())
    notes     = db.Column(db.String())
    summary   = db.Column(db.String())
    
    def __init__(self, user_id, title, course, key_point, notes, summary):
        self.user_id   = user_id
        self.title     = title
        self.course    = course
        self.key_point = key_point
        self.notes     = notes
        self.summary   = summary
    def __repr__(self):
        return '<Note %r>' % (self.title)
