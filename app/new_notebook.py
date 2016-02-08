from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/new_notebook', methods=['GET', 'POST'])
@login_required
def new_notebook():
    if request.method == 'GET':
        return render_template('new_notebook.html', user = g.user, )
    name     =  request.form['name']
    user      =  models.User.query.filter_by(username=g.user.username).first()
    notebook = models.Notebook(user.id, name)
    db.session.add(notebook)
    db.session.commit()
    flash('Notebook succesfully added')
    #TODO change this to view all notes
    return redirect(url_for('all_notes'))
