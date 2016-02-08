from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required
import datetime
@app.route('/new_task', methods=['GET', 'POST'])
@login_required
def new_task():
    if request.method == 'GET':
        return render_template('new_task.html', user = g.user,)
    title       =  request.form['title']
    description =  request.form['description']
    date    =  request.form['date_due']
    print(type(date))
    year, month, day = map(int, date.split('-'))
    date_due = datetime.datetime(year, month, day)
    task = models.Todo(title, description, date_due, g.user.id)
    db.session.add(task)
    db.session.commit()
    flash('task succesfully added')
    #TODO change this to view all notes
    return redirect(url_for('all_notes'))
@app.route('/delete_task/<id>', methods = ['GET'])
@login_required
def delete_task(id):
    task = models.Todo.query.get(id)
    if task is None or task.user_id != g.user.id:
        return redirect(url_for('all_notes'))
    models.Todo.query.filter_by(id=id).delete()
    db.session.commit()
    flash('task deleted')
    return redirect(url_for('all_notes'))


@app.route('/done/<id>', methods=['GET'])
@login_required
def done(id):
    task = models.Todo.query.get(id)
    if task is None or task.user_id != g.user.id:
        return(redirect(url_for('all_notes')))
    task.is_done = True
    db.session.commit()
    return (redirect(url_for('all_notes')))

@app.route('/not_done/<id>')
@login_required
def not_done(id):
    task = models.Todo.query.get(id)
    if task is None or task.user_id != g.user.id:
        return(redirect(url_for('all_notes')))
    task.is_done = False
    db.session.commit()
    return (redirect(url_for('all_notes')))

