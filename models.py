from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# -------------------- USER MODEL --------------------
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Hashed password

    # Relationships
    history = db.relationship('ListeningHistory', backref='user', lazy=True)
    mood_logs = db.relationship('MoodLog', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

# -------------------- SONG MODEL --------------------
class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(120), nullable=True)
    mood_tag = db.Column(db.String(50), nullable=False)  # e.g., happy, sad
    api_source_id = db.Column(db.String(200), nullable=True)  # From external API

    def __repr__(self):
        return f"<Song {self.title}>"

# -------------------- LISTENING HISTORY --------------------
class ListeningHistory(db.Model):
    __tablename__ = 'listening_history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    played_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    song = db.relationship('Song', backref='playbacks')

    def __repr__(self):
        return f"<History user={self.user_id} song={self.song_id}>"

# -------------------- MOOD LOG MODEL --------------------
class MoodLog(db.Model):
    __tablename__ = 'mood_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    detected_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<MoodLog user={self.user_id} mood={self.mood}>"
