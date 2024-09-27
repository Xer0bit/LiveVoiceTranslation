import threading
import queue
import logging
import signal
import time
from flask import Flask, render_template
from flask_socketio import SocketIO
from listener import continuous_listening
from translator import continuous_translation

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log"),
    logging.StreamHandler()
])

app = Flask(__name__)
socketio = SocketIO(app)

sentence_queue = queue.Queue(maxsize=100)  # Adding maxsize to avoid infinite queue
stop_event = threading.Event()

@app.route('/')
def index():
    return render_template('index.html')

def listener_thread(sentence_queue, stop_event):
    continuous_listening(sentence_queue, stop_event)

def translator_thread(sentence_queue, socketio, stop_event):
    continuous_translation(sentence_queue, socketio, stop_event)

def signal_handler(sig, frame):
    logging.info("Signal received, stopping threads...")
    stop_event.set()
    listener_t.join()
    translator_t.join()
    logging.info("Threads stopped, exiting.")
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    listener_t = threading.Thread(target=listener_thread, args=(sentence_queue, stop_event))
    translator_t = threading.Thread(target=translator_thread, args=(sentence_queue, socketio, stop_event))
    
    listener_t.start()
    logging.info("Listener thread started.")
    translator_t.start()
    logging.info("Translator thread started.")
    
    socketio.run(app, debug=True)
