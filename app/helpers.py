import os
import requests
import whisper
from langdetect import detect

class AudioTranscriber:
    def __init__(self, output_path="audio_files"):
        self.output_path = output_path
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def download_audio(self, url, filename="audio.mp3"):
        response = requests.get(url)
        audio_file_path = os.path.join(self.output_path, filename)
        with open(audio_file_path, 'wb') as file:
            file.write(response.content)
        return audio_file_path

    def transcribe_audio(self, audio_path):
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result["text"]

    def detect_language(self, text):
        return detect(text)

    def create_and_open_txt(self, text, filename):
        with open(filename, "w") as file:
            file.write(text)
        self.startfile(filename)

    def startfile(self, filepath):
        os.system(f'open {filepath}' if os.name == 'posix' else f'start {filepath}')
