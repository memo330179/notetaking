from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/new_note', methods=['GET', 'POST'])
@login_required
def new_note():
    if request.method == 'GET':
        notebooks = models.Notebook.query.filter_by(user_id = g.user.id).all()
        return render_template('new_note.html', user = g.user, notebooks = notebooks,)
    title     =  request.form['title']
    notes     =  request.form['notes']
    notebook_id  =  request.form['notebook']
    user   =  models.User.query.filter_by(username=g.user.username).first()
    note = models.Note(title,"", notes,"", notebook_id, g.user.id)
    db.session.add(note)
    db.session.commit()
    flash('Note succesfully added')
    #TODO change this to view all notes
    return redirect(url_for('all_notes'))
