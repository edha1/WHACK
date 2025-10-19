from google.cloud import translate_v2 as translate

# Initialize the client once
translate_client = translate.Client()

def translate_to_english(data: dict) -> dict:
    translated_data = {}

    # Translating header
    translated_header = translate_client.translate(
        data['header'], target_language='en'
    )['translatedText']

    # Translating content
    translated_content = translate_client.translate(
        data['content'], target_language='en'
    )['translatedText']

    # Overwriting data keys
    translated_data['header'] = translated_header
    translated_data['content'] = translated_content
    translated_data['language'] = 'en'

    return translated_data