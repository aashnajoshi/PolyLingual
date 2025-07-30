# PolyLingual
PolyLingual is an intelligent Python-based language translation tool that detects the source language and translates text between multiple languages in real time. It leverages advanced NLP models for accurate, fast translations and offers both single-sentence and batch processing options, enhancing productivity for users who work with multilingual content.

## Features
- **Automatic language detection and translation** between numerous languages.
- **Real-time translation** for single sentences.
- **Batch processing** capability to translate multiple lines or files simultaneously.
- **Easy-to-use command line interface** for efficient productivity.
- **Extensible design** for integrating other NLP models or translation backends.

## Usage
### Basic setup and dependency management:
- Install `pipenv`:
```bash
pip install pipenv
```
- Activate the Virtual Environment:
```bash
pipenv shell
```
- Install required libraries from the `Pipfile.lock`:
```bash
pipenv install
```

### While to run the code:
#### Console-based version:
```bash
python main.py
```
#### Streamlit-based version:
```bash
streamlit run app.py
```

## Description of various files:
- **main.py:** Main application script. Contains function-based views for scraping reviews, analyzing sentiment, and rendering the UI.
- **app.py**: Streamlit based version of the app.
- **Pipfile**: Defines all top-level project dependencies in a structured format.
- **Pipfile.lock**: Locks the exact versions of installed dependencies for consistent environments.
