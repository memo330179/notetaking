from flask import render_template, g, redirect, flash, request, url_for
from app import app, db, models
from flask.ext.login import login_required

@app.route('/delete/<id>', methods=['GET'])
@login_required
def delete_note(id):
    note = models.Note.query.get(id)
    if note is None and note.user_id != g.user.id:
        return redirect(url_for('all_notes'))
    models.Note.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Note succesfully deleted')
    #TODO change this to view all notes
    return redirect(url_for('all_notes'))

@app.route('/delete/notebook/<id>', methods=['GET'])
@login_required
def delete_notebook(id):
    notebook = models.Notebooks.query.get(id)
    if notebook is None and notebook.user_id != g.user.id:
        return redirect(url_for('all_notes'))
    models.Notebook.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Notebook Deleted')
    return redirect(url_for('all_notes'))
