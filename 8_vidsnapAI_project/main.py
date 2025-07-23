from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os
import threading
import time
import subprocess
from text_to_audio import text_to_speech_file

UPLOAD_FOLDER = '8_vidsnapAI_project/user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []

        for key, value in request.files.items():
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                save_dir = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
                os.makedirs(save_dir, exist_ok=True)
                file.save(os.path.join(save_dir, filename))
                input_files.append(filename)

        # Save desc
        with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"), "w") as f:
            f.write(desc)

        # Save input.txt
        for fl in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n")

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("8_vidsnapAI_project/static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)


# 🔁 Background reel creation process
def text_to_audio(folder):
    print("🎤 Converting text to audio for:", folder)
    with open(f"8_vidsnapAI_project/user_uploads/{folder}/desc.txt", "r") as f:
        text = f.read()
    text_to_speech_file(text, folder)

def create_reel(folder):
    command = f'''ffmpeg -f concat -safe 0 -i 8_vidsnapAI_project/user_uploads/{folder}/input.txt -i 8_vidsnapAI_project/user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p 8_vidsnapAI_project/static/reels/{folder}.mp4'''
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ Reel created for: {folder}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating reel for {folder}: {e}")

def background_worker():
    while True:
        print("🚀 Checking for new folders...")
        done_file_path = "8_vidsnapAI_project/done.txt"
        os.makedirs(os.path.dirname(done_file_path), exist_ok=True)
        if not os.path.exists(done_file_path):
            open(done_file_path, 'w').close()
        with open(done_file_path, "r") as f:
            done_folders = f.read().splitlines()

        folders = os.listdir("8_vidsnapAI_project/user_uploads")
        for folder in folders:
            if folder not in done_folders:
                text_to_audio(folder)
                create_reel(folder)
                with open(done_file_path, "a") as f:
                    f.write(folder + "\n")
        time.sleep(4)


# 🚀 Launch both Flask and background thread
if __name__ == "__main__":
    threading.Thread(target=background_worker, daemon=True).start()
    app.run(host='0.0.0.0', port=10000)
