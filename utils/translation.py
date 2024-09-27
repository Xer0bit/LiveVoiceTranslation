import requests
import uuid
import logging

def translate_text(text, translator_key, translator_endpoint, translator_location):
    logging.info(f"Translating text: {text}")  # Log the text to be translated

    path = '/translate'
    constructed_url = translator_endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['fr']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': translator_key,
        'Ocp-Apim-Subscription-Region': translator_location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': text}]

    try:
        response = requests.post(constructed_url, params=params, headers=headers, json=body)
        response.raise_for_status()
        response_json = response.json()
        logging.debug("API response received successfully.")

        if response_json and 'translations' in response_json[0]:
            translated_text = response_json[0]['translations'][0]['text']
            logging.info(f"Translated text: {translated_text}")  # Log the translated text
            return translated_text
        else:
            logging.error("No translations found in the response.")
            return ""
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return ""
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return ""
