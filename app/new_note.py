from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/newnote', methods=['GET', 'POST'])
@login_required
def new_note():
    if request.method == 'GET':
        return render_template('new_note.html')
    title     =  request.form['title']
    course    =  request.form['course']
    key_point =  request.form['key_point']
    notes     =  request.form['notes']
    summary   =  request.form['summary']
    user      =  models.User.query.filter_by(username=g.user.username).first()
    note = models.Note(user.id, title, course, key_point, notes, summary)
    db.session.add(note)
    db.session.commit()
    flash('Note succesfully added')
    #TODO change this to view all notes
    return redirect(url_for('index'))
