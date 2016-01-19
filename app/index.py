from flask import Flask
from app import app
from flask.ext.login import login_required

@app.route("/")
@app.route("/index")
@login_required
def index():
    return "hello world"
