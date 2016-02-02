from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required, current_user

@app.route('/all_notes', methods=['GET'])
@login_required
def all_notes():
    notebooks = models.Notebook.query.filter_by(user_id = g.user.id).all()
    tasks     = models.Todo.query.filter_by(user_id = g.user.id).all()
    notes = [] 
    for course in notebooks:
        note = models.Note.query.filter_by(course_id = course.id).all()
        notes.extend(note)
    return render_template("all_notes.html", notebooks = notebooks, notes = notes, user = g.user, tasks=tasks)
