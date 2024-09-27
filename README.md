# VocalTranslate-Voice-to-Text-Translator

## Description
VocalTranslate is a project designed to convert spoken language into written text and then translate that text into a target language. This repository contains the code and resources needed to implement a seamless voice-to-text translation system, making language barriers a thing of the past. Whether you are developing an app for travelers, a tool for international business communication, or an aid for language learners, VocalTranslate offers a robust solution for real-time language translation.

## Features
- **Voice Input:** Capture spoken words through a microphone.
- **Text Conversion:** Convert voice input into written text with high accuracy.
- **Language Translation:** Translate the converted text into a desired target language.
- **Multi-Language Support:** Supports a wide range of languages for both input and output.
- **User-Friendly Interface:** Easy to use and integrate into various applications.

## Technologies Used
- **Azure Speech Service API:** For capturing and converting voice input.
- **Azure Translator API:** For translating text into the target language.
- **Frontend Frameworks:** For building user-friendly interfaces.
- **Backend Services:** For processing and managing the translation workflow.

## Getting Started
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/xer0bit/VocalTranslate-Voice-to-Text-Translator.git
    ```

2. **Install Dependencies:**
    ```bash
    cd VocalTranslate-Voice-to-Text-Translator
    pip install requirement.txt
    ```

3. **Set Up Azure API Keys:**
    - Obtain API keys for the Azure Speech Service and Azure Translator from the [Azure Portal](https://portal.azure.com/).
    - Configure the API keys in the `configs\azure_credentials.json` file:
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

4. **Run the Application:**
    ```bash
    python ui.py
    ```

## Usages
VocalTranslate can be used in various scenarios, including but not limited to:
- Translating subtitles in live streams or movies.
- Assisting travelers by providing real-time translation.
- Facilitating international business communication.
- Helping language learners understand and practice new languages.

## Contributing
We welcome contributions from the community! Feel free to open issues, submit pull requests, or suggest new features.

## License
This project is licensed under the MIT License.
