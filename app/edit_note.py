from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/note/edit/note/<id>', methods=['GET', 'POST'])
@login_required
def edit_note(id):
    if request.method == 'GET':
        note = models.Note.query.get(id)
        return render_template('edit_note.html', note = note, user = g.user,)
    note = models.Note.query.get(id)
    
    note.title     = request.form['title']
    note.course    = request.form['course']
    note.notes     = request.form['notes']
    db.session.commit()
    
    return redirect(url_for('note', id=id))

@app.route('/note/edit/summary/<id>', methods=['GET', 'POST'])
@login_required
def edit_summary(id):
    if request.method == 'GET':
        note = models.Note.query.get(id)
        return render_template('edit_summary.html', note = note, user = g.user,)
    note = models.Note.query.get(id)
    
    note.summary   = request.form['summary']
    db.session.commit()
    
    return redirect(url_for('note', id=id))

@app.route('/note/edit/key_points/<id>', methods=['GET', 'POST'])
@login_required
def edit_key_points(id):
    if request.method == 'GET':
        note = models.Note.query.get(id)
        return render_template('edit_key_point.html', note = note, user = g.user,)
    note = models.Note.query.get(id)
    
    note.key_point   = request.form['key_point']
    db.session.commit()
    
    return redirect(url_for('note', id=id))
