# 🎬 VidsnapAI – AI-Powered Reel Generator

VidsnapAI is a simple and smart web application built using Python and Flask. It allows users to upload images and a short description. Then it automatically creates a video reel (`.mp4`) by converting the description into voice (using text-to-speech) and combining it with the uploaded images.

---

## 🚀 Features

- 📤 Upload multiple images (in correct order)
- 📝 Enter a short description (used as voiceover)
- 🗣️ Converts text to speech using Google TTS (`gTTS`)
- 🎥 Automatically creates a vertical 1080x1920 reel using `ffmpeg`
- 🖼️ View and play your generated reel in a gallery
- 🔄 Periodically checks and processes new uploads

---

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| **Python** | Main programming language |
| **Flask** | Web framework for backend |
| **HTML, CSS (Jinja2)** | Frontend and template rendering |
| **gTTS** | Converts text to speech (Google Text-to-Speech) |
| **ffmpeg** | Combines audio and images to create `.mp4` video |
| **os, subprocess, uuid** | For folder creation, video processing, and unique names |

---

## 🧱 Project Structure

```
8_vidsnapAI_project/
│
├── main.py                 # Main Flask application (handles routes and logic)
├── generate_process.py     # Combines images + audio into video using ffmpeg
├── text_to_audio.py        # Converts text to speech using gTTS and saves as audio.mp3
├── done.txt                # Keeps track of already processed folders
├── input.txt               # Used by ffmpeg for concatenation
│
├── user_uploads/           # Contains user-submitted folders with images + description
│   └── <unique_folder_id>/ # Each upload folder (with images, description.txt, audio.mp3)
│
├── static/
│   ├── reels/              # Stores generated video reels (.mp4)
│   ├── css/
│   │   ├── style.css       # Common styling
│   │   ├── create.css      # Styling for create.html page
│   │   └── gallery.css     # Styling for gallery.html page
│   └── sample_images/      # (Optional) Store any static sample images if used
│
├── templates/
│   ├── base.html           # Base layout using Jinja2
│   ├── index.html          # Homepage
│   ├── create.html         # Form for uploading images and description
│   └── gallery.html        # Displays all generated reels
│
└── README.md               # Documentation file (you’re preparing this!)

```

## 🧪 How It Works

1. Run `app.py` to start the Flask web interface:
   ```bash
   python app.py
2.Go to http://127.0.0.1:5000 to:
    Upload images + description
    See reels in the gallery

