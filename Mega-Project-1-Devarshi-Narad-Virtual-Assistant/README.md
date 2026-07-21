# Mega Project 1 — Devarshi Narad (Virtual Assistant)

A voice-controlled desktop virtual assistant named **Narad**, built in Python. It listens for a wake word, processes spoken commands, and responds using text-to-speech — similar in concept to Alexa or Siri.

## Features
- Wake-word detection ("Narad") using a microphone
- Opens websites (Google, YouTube, Facebook, LinkedIn) on voice command
- Plays songs from a personal music library by name
- Fetches and reads out the latest news headlines via the News API
- Falls back to **Gemini AI** (Google GenAI) for general conversational commands

## Tech stack
| Library | Purpose |
|---|---|
| `speech_recognition` | Captures and transcribes voice input |
| `gTTS` + `pygame` | Converts responses to speech and plays them |
| `pyttsx3` | Offline TTS fallback (older implementation) |
| `pywhatkit` | Plays YouTube videos by search query |
| `requests` | Fetches news from the News API |
| `google-genai` | Gemini AI for general command processing |
| `python-dotenv` | Loads API keys from a `.env` file |

## Setup
```bash
pip install -r requirements.txt
```

Create a `.env` file in this folder with your API keys:
```
GEMINI_API_KEY=your_gemini_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

Then run:
```bash
python3 assistant.py
```

## Files
- `assistant.py` — main assistant logic: wake-word loop, command processing, speech output
- `musicLibrary.py` — dictionary mapping song names to YouTube URLs

## Concepts applied
Modules, dictionaries, functions, API integration, `os`/`dotenv` for secrets — drawing on Chapters 5, 8, and external libraries.
