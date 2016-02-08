from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/note/edit/note/<id>', methods=['GET', 'POST'])
@login_required
def edit_note(id):
    note = models.Note.query.get(id)
    if note is None or note.user_id != g.user.id:
        return redirect(url_for('all_notes'))
    if request.method == 'GET':
        notebooks = models.Notebook.query.filter_by(user_id = g.user.id).all()
        return render_template('edit_note.html', note = note, user = g.user, notebooks=notebooks,)

    note.title     = request.form['title']
    note.notebook_id    = request.form['notebook']
    note.notes     = request.form['notes']
    db.session.commit()

    return redirect(url_for('note', id=id))

@app.route('/note/edit/summary/<id>', methods=['GET', 'POST'])
@login_required
def edit_summary(id):
    note = models.Note.query.get(id)
    if note is None or note.user_id != g.user.id:
        return redirect(url_for('all_notes'))
    if request.method == 'GET':
        return render_template('edit_summary.html', note = note, user = g.user,)

    note.summary   = request.form['summary']
    db.session.commit()

    return redirect(url_for('note', id=id))

@app.route('/note/edit/key_points/<id>', methods=['GET', 'POST'])
@login_required
def edit_key_points(id):
    note = models.Note.query.get(id)
    if note is None or note.user_id != g.user.id:
        return redirect(url_for('all_notes'))
    if request.method == 'GET':
        return render_template('edit_key_point.html', note = note, user = g.user,)

    note.key_point   = request.form['key_point']
    db.session.commit()

    return redirect(url_for('note', id=id))
