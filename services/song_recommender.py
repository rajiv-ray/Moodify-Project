import random
from ytmusicapi import YTMusic
import yt_dlp

# Initialize YTMusic
ytmusic = YTMusic()

def get_audio_url(video_id):
    """Fetch direct audio URL using yt_dlp."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'extract_flat': False
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
        return info['url']

def recommend_songs(mood):
    """Recommend songs based on mood."""
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
        # Search for songs on YouTube Music
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

        # Fallback if no results found
        if not songs:
            fallback = ytmusic.search("top hindi songs", filter='songs', limit=10)
            for r in fallback:
                if 'videoId' in r:
                    songs.append({
                        "title": r['title'],
                        "artist": ', '.join([a['name'] for a in r['artists']]),
                        "videoId": r['videoId'],
                        "thumbnail": r['thumbnails'][0]['url']
                    })
#shuffle songs
        random.shuffle(songs)
        return songs[:5]
    except Exception as e:
        print(f"[ERROR] YTMusic search failed: {e}")
        return []

if __name__ == "__main__":
    print("Functions available:", [f for f in dir() if not f.startswith("_")])