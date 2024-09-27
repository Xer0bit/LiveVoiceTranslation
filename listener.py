import time
import logging
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig, ResultReason
from utils.credentials import load_credentials

def initialize_recognizer():
    credentials = load_credentials()
    if not credentials:
        logging.error("Failed to load credentials, exiting.")
        return None

    speech_key = credentials['speech_service']['subscription_key']
    service_region = credentials['speech_service']['region']
    speech_config = SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = AudioConfig(use_default_microphone=True)

    return SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

def continuous_listening(sentence_queue, stop_event):
    recognizer = initialize_recognizer()
    if not recognizer:
        return

    last_result = None

    def recognized(evt):
        nonlocal last_result
        if evt.result.reason == ResultReason.RecognizedSpeech and evt.result.text and evt.result.text != last_result:
            logging.info(f"Recognized: {evt.result.text}")
            last_result = evt.result.text
            sentence_queue.put(evt.result.text)
        else:
            logging.warning(f"Speech Recognition Error or Ignored Phrase: {evt.result.text}")

    recognizer.recognized.connect(recognized)
    logging.info("Listening...")

    recognizer.start_continuous_recognition()

    try:
        while not stop_event.is_set():
            time.sleep(0.1)
    except KeyboardInterrupt:
        logging.info("Stopped by user")
    finally:
        recognizer.stop_continuous_recognition()
        logging.info("Continuous recognition stopped.")
