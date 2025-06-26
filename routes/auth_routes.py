from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import User  # assuming User model is already defined
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth_bp', __name__)

# ------------------ LOGIN ------------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('player_bp.dashboard'))  # redirect to dashboard
        else:
            flash('Invalid username or password')
            return redirect(url_for('auth_bp.login'))

    return render_template('login.html')


# ------------------ REGISTER ------------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # You may want to hash password here and add validation
        flash('Registered successfully (placeholder, DB work not implemented)')
        return redirect(url_for('auth_bp.login'))

    return render_template('register.html')


# ------------------ LOGOUT ------------------
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
