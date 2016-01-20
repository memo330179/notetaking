from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/edit/note/<id>', methods=['GET', 'POST'])
@login_required
def edit_note(id):
    if request.method == 'GET':
        note = models.Note.query.get(id)
        return render_template('edit_note.html', note = note, user = g.user,)
    note = models.Note.query.get(id)
    
    note.title     = request.form['title']
    note.course    = request.form['course']
    note.key_point = request.form['key_point']
    note.notes     = request.form['notes']
    note.summary   = request.form['summary']
    db.session.commit()
    
    return render_template("edit_note.html", note = note, user = g.user,)
