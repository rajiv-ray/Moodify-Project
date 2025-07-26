from fer import FER
from ytmusicapi import YTMusic
import yt_dlp

# Emotion detector instance
detector = FER()

# YTMusic instance
ytmusic = YTMusic()

# Audio URL extractor
def get_audio_url(video_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'extract_flat': False
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
        return info['url']
