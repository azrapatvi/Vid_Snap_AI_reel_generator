🎬 VidsnapAI – AI-Powered Reel Generator
VidsnapAI is a simple yet powerful web application built using Python and Flask. It allows users to upload images and provide a short description, which is then converted into a voiceover using text-to-speech. The application automatically combines the images and voice to generate a vertical video reel in .mp4 format.

🚀 Features
📤 Upload multiple images in the correct order

📝 Add a short description (used as voiceover)

🗣️ Converts text to speech using Google TTS (gTTS)

🎥 Automatically creates vertical 1080x1920 reels using FFmpeg

🖼️ View and play your generated reels in a gallery

🔄 Periodically checks and processes new uploads

🛠️ Technologies Used
Tool/Library	Purpose
Python	Main programming language
Flask	Web framework for backend
HTML, CSS, Jinja2	Frontend and template rendering
gTTS	Google Text-to-Speech (converts text to audio)
ffmpeg	Combines images and audio into .mp4 video
os, subprocess, uuid	Folder creation, video processing, unique naming

🧱 Project Structure
```
8_vidsnapAI_project/
│
├── main.py               # Main Flask app (handles routes and logic)
├── generate_process.py   # Combines images + audio into video using ffmpeg
├── text_to_audio.py      # Converts text to speech using gTTS
├── done.txt              # Tracks already processed folders
├── input.txt             # Used by ffmpeg for video concatenation
│
├── user_uploads/         # Contains user-submitted folders (images + text)
│   └── <unique_folder_id>/
│       ├── image1.jpg, image2.jpg, ...
│       ├── description.txt
│       └── audio.mp3
│
├── static/
│   ├── reels/            # Stores generated reels (.mp4)
│   ├── css/
│   │   ├── style.css     # Common styling
│   │   ├── create.css    # Styling for create page
│   │   └── gallery.css   # Styling for gallery page
│   └── sample_images/    # Optional: sample assets
│
├── templates/
│   ├── base.html         # Base layout using Jinja2
│   ├── index.html        # Homepage
│   ├── create.html       # Form for uploading
│   └── gallery.html      # Gallery to view generated reels
│
└── README.md             # This documentation
```

🧪 How It Works
1)Run the application:
    python app.py

2)Open your browser and go to:
    http://127.0.0.1:5000
    
3)From the web interface, you can:
    Upload images and a short description
    View all generated video reels in the gallery

