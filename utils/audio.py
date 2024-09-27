import pyaudio
import logging

def initialize_audio():
    try:
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=16000,
                            input=True,
                            frames_per_buffer=512)
        return audio, stream
    except Exception as e:
        logging.error(f"Error initializing audio: {e}")
        return None, None
