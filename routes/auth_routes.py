from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth = Blueprint('auth', __name__)

# ------------------ LOGIN ------------------
@auth.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('player.dashboard'))  # Redirect to dashboard
        else:
            flash('Invalid Email or Password', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

# ------------------ REGISTER ------------------
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please login.', 'error')
            return redirect(url_for('auth.login'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=name, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Registered successfully. Please Login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


# ------------------ LOGOUT ------------------
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))