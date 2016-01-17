import os
from flask import Flask, g


app = Flask(__name__)

@app.before_request
def before_request():
    g.db = database
    g.db.connect()
    
@app.after_request
def after_request(response):
    g.db.close()
    return response
    
app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))

from app import index
from app import register



