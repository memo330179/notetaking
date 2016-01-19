from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/all_notes', methods=['GET'])
@login_required
def all_notes():
    notes = models.Note.query.filter_by(user_id = g.user.id).all()
    
    return render_template("all_notes.html", notes = notes,)
