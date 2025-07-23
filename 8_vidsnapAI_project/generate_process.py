# This file looks for new folders inside user uploads and converts them to reels if not already converted
import os
import time
import subprocess
from text_to_audio import text_to_speech_file

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
        print(f"📍 Path: 8_vidsnapAI_project/static/reels/{folder}.mp4")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating reel for {folder}: {e}")

if __name__ == "__main__":
    while True:
        print("🚀 Checking for new folders...")
        with open("8_vidsnapAI_project/done.txt", "r") as f:
            done_folders = f.read().splitlines()

        folders = os.listdir("8_vidsnapAI_project/user_uploads")
        for folder in folders:
            if folder not in done_folders:
                text_to_audio(folder)
                create_reel(folder)
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(4)
