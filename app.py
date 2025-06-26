from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, User  # You still need to coordinate with DB teammate

app = Flask(__name__)

# ----------------- Configuration -----------------
app.config['SECRET_KEY'] = 'k4!GzW8@9#bX2vQ1%LmTp7$dY&FsNj4^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ----------------- Initialize Extensions -----------------
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# ----------------- User Loader -----------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ----------------- Register Routes -----------------
from routes.auth_routes import auth_bp
from routes.player_routes import player_bp

app.register_blueprint(auth_bp)
app.register_blueprint(player_bp)

# ----------------- Run App -----------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Your DB teammate can handle migrations later
    app.run(debug=True)
