from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/note/<id>', methods=['GET'])
@login_required
def note(id):
    note = models.Note.query.get(id)
    
    return render_template("note.html", note = note,)
