from app import app, db, models
from flask import redirect, url_for, request, render_template, flash, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

@app.before_request
def before_request():
    g.user = current_user
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', )
    username = request.form['username']
    password = request.form['password']
    registered_user = models.User.query.filter_by(username=username).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    if registered_user and registered_user.check_password(password):
        login_user(registered_user)
        flash('Logged in successfully')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
