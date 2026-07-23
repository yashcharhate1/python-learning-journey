# Mega Project 2 — Auto Reply AI Chatbot (WhatsApp)

An AI-powered desktop tool that reads a WhatsApp chat window, parses the conversation history, generates a context-aware reply using Gemini AI, and types it automatically — simulating how a real person would respond.

## How it works
1. A keyboard shortcut triggers the bot.
2. The bot copies the visible WhatsApp chat text from the screen using `pyautogui` and `pyperclip`.
3. The chat log is parsed into a structured list of `(sender, message)` tuples — handling multi-line messages and WhatsApp's timestamp format.
4. The full conversation history is sent to Gemini AI with a persona prompt ("You are Yash, a coder from India...").
5. The AI-generated reply is typed back into the WhatsApp input field automatically.

## Tech stack
| Library | Purpose |
|---|---|
| `google-genai` | Gemini AI for generating replies |
| `pyautogui` | Controls the mouse and keyboard |
| `pyperclip` | Reads clipboard content |
| `keyboard` | Detects the trigger hotkey |
| `python-dotenv` | Loads the Gemini API key from `.env` |

## Setup
```bash
pip install -r requirements.txt
```

Create a `.env` file in this folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

Then run:
```bash
python3 bot.py
```

## Files
- `bot.py` — main bot loop: keyboard trigger, screen capture, chat parsing, auto-reply
- `gemini.py` — Gemini AI client wrapper for generating responses
- `get_cursor.py` — utility to detect and return the current cursor position on screen

## Concepts applied
Regex, string parsing, functions, API integration, `os`/`dotenv` — drawing on Chapters 8, 12, 13, and external libraries.

> **Note:** This project requires WhatsApp Web open in a browser and proper screen coordinates configured for your display setup.
