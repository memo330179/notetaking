from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash

db = SqliteDatabase('notes.db')

class BaseModel(Model):
    class Meta:
        database = db 

class User(BaseModel):
    username      = CharField()
    password      = CharField()
    email         = CharField()
    authenticated = BooleanField()
    
    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email    = email
    
    def is_active(self):
        """All user will be active"""
        return True
    
    
    def get_id(self):
        """Return the email address"""
        return self.email
        
    def is_authenticated(self):
        """Return True if the user is authenticated"""
        return self.authenticated
        
    def is_anonymous(self):
        return False
        
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
        
    def __repr__(self):
        return '<User %r>' % (self.username)
    
    class Meta:
        order_by = ('username',)
        
    
        
        
class Relationship(BaseModel):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user   = ForeignKeyField(User, related_name='related_to')
    
    class Meta:
        indexes = (
            (('from_user', 'to_user'), True),
            )
            
class Note(BaseModel):
    user      = ForeignKeyField(User)
    title     = CharField()
    course    = CharField()
    key_point = TextField()
    notes     = TextField()
    summary   = TextField()