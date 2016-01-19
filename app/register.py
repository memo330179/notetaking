from app import app, models, db
from flask import redirect, url_for, request, render_template, flash, g

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
        
    user = models.User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User succesfully registered')
    return redirect(url_for('login'))
