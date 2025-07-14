# backend/player_routes.py

from flask import Blueprint, render_template, request, jsonify, session
from models import db, User  # adjust imports as per your project structure

player_bp = Blueprint('player', __name__, url_prefix='/player')

# Sample: Mood-based song list
@player_bp.route('/mood/<mood>', methods=['GET'])
def get_mood_songs(mood):
    # This should be dynamically fetched from DB or API
    mood_song_map = {
        "happy": ["Zingaat", "Apna Time Aayega"],
        "sad": ["Channa Mereya", "Tadap Tadap"],
        "angry": ["Malhari", "Zinda"],
        "romantic": ["Tum Mile", "Raabta"]
    }
    songs = mood_song_map.get(mood.lower(), [])
    return jsonify({"mood": mood, "songs": songs})

# Sample: Play a song
@player_bp.route('/play', methods=['POST'])
def play_song():
    data = request.get_json()
    song_name = data.get("song")
    # You may integrate audio streaming or return metadata
    return jsonify({"message": f"Playing {song_name}!"})

# Sample: Create a playlist
@player_bp.route('/playlist', methods=['POST'])
def create_playlist():
    data = request.get_json()
    name = data.get("name")
    songs = data.get("songs", [])
    # Logic to save playlist in DB (use session['user_id'] if logged in)
    return jsonify({"message": "Playlist created", "name": name, "songs": songs})
