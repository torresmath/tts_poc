import json
import os.path
from os import getcwd
from typing import Dict

import pyttsx3

speaker = pyttsx3.init()
speaker.setProperty('voice', 'brazil')
save_path = f"{getcwd()}\speech_db"
files_extension = 'wav'

for voice in speaker.getProperty('voices'):
    print(voice)


def safe_check_path(text_data: Dict[str, str]):
    expected_path = f"{save_path}\{text_data['category']}"
    if not os.path.exists(expected_path):
        os.makedirs(expected_path)


def save_pyttex3(text_data: Dict[str, str]):
    text = text_data['text']
    safe_check_path(text_data)
    filename = f"{save_path}\{text_data['category']}\{text_data['id']}.{files_extension}"
    speaker.save_to_file(text=text, filename=filename)
    speaker.runAndWait()
    print(f"Successfully saved audio: {filename}")


if __name__ == '__main__':

    with open('texts_db.json', encoding='utf8') as json_file:
        texts_db = json.load(json_file)

    for content in texts_db['content']:
        # save_gtts(content)
        save_pyttex3(content)
