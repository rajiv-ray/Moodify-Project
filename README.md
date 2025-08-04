# 🎵 Facial Mood-Based Music Player

A Flask-powered web application that detects facial mood and plays music based on your emotional state.

---

## 🚀 Features

- 🎭 Facial Expression Detection (via OpenCV)
- 🎶 Music Playlist Generator (via music API)
- 👤 User Login & Registration (sqlite database)
- 🧠 Mood-based Animated Emojis
- 🎨 Dynamic Background Changes Based on Mood
- 📊 Dashboard with Song History & Mood Analytics

---

## 🛠 Tech Stack

- **Backend:** Python, Flask, Flask-Login, Flask-SQLAlchemy
- **Frontend:** HTML, CSS, JS
- **Database:** sqlite
- **Libraries:** OpenCV, PyMySQL
- **Team Collaboration:** GitHub, GitHub Desktop, Branching

---

## 🧑‍💻 How to Run (For Devs)

```bash
# 1. Clone the repo
git clone https://github.com/rajiv-ray/Moodify-Project.git
cd project-folder

# 2. Create & activate virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
