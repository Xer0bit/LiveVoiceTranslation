import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_credentials(filepath='configs/azure_credentials.json'):
    if not Path(filepath).exists():
        logging.error(f"File not found: {filepath}")
        return None

    try:
        with open(filepath) as f:
            credentials = json.load(f)
            logging.debug(f"Credentials loaded successfully from {filepath}")
            return credentials
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from {filepath}: {e}")
        return None
    except Exception as e:
        logging.error(f"An error occurred while loading credentials from {filepath}: {e}")
        return None

if __name__ == "__main__":
    creds = load_credentials()
    if creds:
        logging.info("Credentials: %s", creds)
    else:
        logging.error("Failed to load credentials.")
