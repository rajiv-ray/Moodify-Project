from flask import Blueprint, request, redirect, jsonify, render_template
from models import db, User
from utils import ytmusic, get_audio_url
import random
from services.mood_detector import detect_mood_from_base64


player = Blueprint('player', __name__, url_prefix='/player')

# Track already played songs to avoid repetition
played_songs = {"happy": [], "sad": [], "neutral": []}

# ------------------ DASHBOARD ----------------
@player.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@player.route('/detect_mood', methods=['POST'])
def detect_mood():
    try:
        data = request.get_json()
        img_data = data.get('image')

        print("Received image data:", img_data[:100])

        if not img_data:
            return jsonify({"error": "No image data received"}), 400

        # Detect mood from image
        emotion, confidence = detect_mood_from_base64(img_data)

        return jsonify({
            "mood": emotion,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@player.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get("mood", "neutral").lower()

    mood_to_query = {
        "happy": "latest happy hindi songs",
        "sad": "sad hindi songs",
        "neutral": "relaxing hindi songs",
        "angry": "motivational hindi songs",
        "fear": "calm soothing hindi songs",
        "surprise": "party hindi songs"
    }
    query = mood_to_query.get(mood, "hindi songs")

    songs = []
    try:
        results = ytmusic.search(query, filter='songs', limit=10)
        for r in results:
            if 'videoId' not in r:
                continue
            songs.append({
                "title": r['title'],
                "artist": ', '.join([a['name'] for a in r['artists']]),
                "videoId": r['videoId'],
                "thumbnail": r['thumbnails'][0]['url']
            })

        if not songs:
            results = ytmusic.search("top hindi songs", filter='songs', limit=10)
            for r in results:
                if 'videoId' in r:
                    songs.append({
                        "title": r['title'],
                        "artist": ', '.join([a['name'] for a in r['artists']]),
                        "videoId": r['videoId'],
                        "thumbnail": r['thumbnails'][0]['url']
                    })

        random.shuffle(songs)
        selected_songs = songs[:5]

    except Exception as e:
        print(f"[ERROR] YTMusic search failed: {e}")
        selected_songs = []

    return jsonify({"songs": selected_songs})


@player.route('/play/<video_id>')
def play(video_id):
    try:
        audio_url = get_audio_url(video_id)
        return jsonify({"audio_url": audio_url})
    except Exception as e:
        print(f"[ERROR] yt_dlp failed: {e}")
        return jsonify({"error": "Audio extraction failed"}), 500
