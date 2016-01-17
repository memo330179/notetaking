from app import app, db, models
from flask import redirect, url_for, request, render_template, flash, g
from flask.ext.login import login_user, logout_user, current_user, login_required

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
        
    user = User(request.form['username'], request.form['password'], request.form['email'])
    user.save()
    flash('User succesfully registered')
    return redirect(url_for('login'))