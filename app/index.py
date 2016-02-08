from flask import Flask, render_template, flash, g, redirect, url_for
from app import app
from flask.ext.login import login_required

@app.route("/")
@app.route("/index")
def index():
    return redirect(url_for('all_notes'))
