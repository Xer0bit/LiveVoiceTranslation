**VocalTranslate - Voice-to-Text Translator (Web-Based)**
======================================================

**Description**
---------------

VocalTranslate is a web-based application designed to convert spoken language into written text and then translate that text into a target language. By leveraging Flask API, this solution provides real-time translation accessible
through any web interface.

### Features

* **Voice Input**: Capture spoken words via a web-based microphone interface.
* **Text Conversion**: Convert voice input into written text with high accuracy.
* **Language Translation**: Translate the text into a desired target language.
* **Multi-Language Support**: Supports numerous languages for both input and output.
* **Web-Based Interface**: Accessible from any device with a web browser.

**Features**
-------------

### File Structure

* `configs/azure_credentials.json`: Stores the Azure Speech Service and Translator API keys.
* `.templates/`: Contains HTML templates for the web interface.
* `utils/`: Utility functions supporting various components.
* `README.md`: Project documentation.
* `app.log`: Logs related to app performance and errors.
* `listener.py`: Handles the audio input and voice-to-text conversion.
* `logs.txt`: Stores logs of translation and text output.
* `main.py`: The main entry point for running the Flask API.
* `requirement.txt`: List of dependencies needed to run the project.
* `translated_text.txt`: Stores the translated text output.
* `translator.py`: Manages the translation of text into the target language.
* `verify_audio.py`: Handles verification of audio quality and validity.

**Technologies Used**
--------------------

* **Flask API**: For building the web-based application.
* **Azure Speech Service**: For capturing and converting voice input.
* **Azure Translator API**: For translating text into the target language.
* **HTML/CSS**: For building the web interface.
* **Python**: For backend logic and API communication.

**Working Chart**
--------------------
![Flowchart illustrating the steps involved in using VocalTranslate](https://github.com/Xer0bit/LiveVoiceTranslation/blob/main/templates/chart.png)

**Getting Started**
-------------------

### Clone the Repository

```bash
git clone https://github.com/Xer0bit/LiveVoiceTranslation.git
```

### Install Dependencies

```bash
cd LiveVoiceTranslation
pip install -r requirement.txt
```

### Set Up Azure API Keys

Obtain API keys for Azure Speech Service and Azure Translator from the Azure Portal. Configure the API keys in the `configs/azure_credentials.json` file:

```json
{
  "speech_service": {
    "subscription_key": "SPEECH API HERE",
    "region": "TYPE REGION"
  },
  "translator_service": {
    "subscription_key": "TRANSLATION API HERE",
    "endpoint": "TYPE ENDPOINT",
    "location": "TYPE REGION"
  }
}
```

### Run the Application

```bash
python main.py
```

This will start the Flask server, and you can access the web interface by visiting `http://localhost:5000`.

**Usage**
--------

VocalTranslate can be used in various real-world scenarios, such as:

* Real-time translation in live events or streams.
* Assisting travelers with quick and accurate translations.
* Supporting international business meetings with multilingual communication.
* Helping language learners practice and improve their language skills.

**Contributing**
--------------

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest new features.
