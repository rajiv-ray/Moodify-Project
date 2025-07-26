from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager
from models import db, User
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

# ----------------- Configuration -----------------
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ----------------- Initialize Extensions -----------------
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# ----------------- User Loader -----------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ----------------- Register Routes -----------------
from routes.auth_routes import auth
from routes.player_routes import player

app.register_blueprint(auth)
app.register_blueprint(player)

# ----------------- Run App -----------------
if __name__ == '__main__':
    app.run(debug=True, port=8080)