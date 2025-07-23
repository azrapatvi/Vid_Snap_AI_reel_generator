from gtts import gTTS  # or any other TTS lib you use
import os

def text_to_speech_file(text, folder):
    tts = gTTS(text)
    output_path = f"8_vidsnapAI_project/user_uploads/{folder}/audio.mp3"
    tts.save(output_path)
    print(f"✅ Audio saved at: {output_path}")
