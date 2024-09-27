import time
import logging
import queue
from utils.credentials import load_credentials
from utils.translation import translate_text

def continuous_translation(sentence_queue, socketio, stop_event):
    credentials = load_credentials()
    if not credentials:
        logging.error("Failed to load credentials, exiting.")
        return

    translator_key = credentials['translator_service']['subscription_key']
    translator_endpoint = credentials['translator_service']['endpoint']
    translator_location = credentials['translator_service']['location']

    processed_sentences = set()

    while not stop_event.is_set():
        try:
            sentence = sentence_queue.get(timeout=10)
            if sentence and sentence not in processed_sentences:
                logging.info(f"Processing sentence: {sentence}")
                translated_text = translate_text(sentence, translator_key, translator_endpoint, translator_location)
                logging.info(f"Translated text: {translated_text}")
                socketio.emit('new_translation', {'data': translated_text})
                processed_sentences.add(sentence)
                sentence_queue.task_done()
        except queue.Empty:
            logging.debug("No sentences in queue, waiting...")
        except Exception as e:
            logging.error(f"Error translating text: {e}")
        time.sleep(1)
