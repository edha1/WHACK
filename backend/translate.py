import os
import requests

# Load API key for cloud from dotenv
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"

# Translates a single piece of text to English
def translate_text(text: str) -> str:
    response = requests.post(
        TRANSLATE_URL,
        params={'key': API_KEY},
        json={
            'q': text,
            'target': 'en',
            'format': 'text'
        },
        headers={'Content-Type': 'application/json'}
    )
    response.raise_for_status()
    return response.json()['data']['translations'][0]['translatedText']

# Public function used by Flask route
def translate_to_english(data: dict) -> dict:
    return {
        'header': translate_text(data['header']),
        'content': translate_text(data['content']),
        'language': 'en'
    }