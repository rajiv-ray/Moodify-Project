import base64
from io import BytesIO
from PIL import Image
import numpy as np
from fer import FER

# Initialize FER detector
detector = FER()

# Map FER emotions to your app's moods
EMOTION_MAP = {
    'happy': 'happy',
    'sad': 'sad',
    'angry': 'angry',
    'surprise': 'surprise',
    'neutral': 'neutral',
    'fear': 'sad',        # Map 'fear' to 'sad' or 'neutral' as you prefer
    'disgust': 'neutral', # Map 'disgust' to 'neutral'
    'calm': 'neutral'
}

def detect_mood_from_base64(img_data):
    """Detect mood from base64 image data."""
    if not img_data or not img_data.startswith('data:image'):
        raise ValueError("Invalid image data")

    # Decode base64 image
    header, encoded = img_data.split(",", 1)
    img_bytes = base64.b64decode(encoded)
    img = Image.open(BytesIO(img_bytes)).convert('RGB')
    frame = np.array(img)

    # Detect emotions
    results = detector.detect_emotions(frame)
    if results:
        emotions = results[0]['emotions']
        top_emotion = max(emotions, key=emotions.get)
        confidence = emotions[top_emotion]
        # Map to supported moods
        mood = EMOTION_MAP.get(top_emotion, 'neutral')
    else:
        mood, confidence = "neutral", 0.5

    return mood, confidence