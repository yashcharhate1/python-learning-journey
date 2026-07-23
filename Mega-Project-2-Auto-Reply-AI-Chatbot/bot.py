import os
import re
import time

import keyboard
import pyautogui
import pyperclip
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=GEMINI_API_KEY)

MESSAGE_LINE_RE = re.compile(
    r"^\[\d{1,2}:\d{2}\s*[ap]m,\s*\d{1,2}/\d{1,2}/\d{2,4}\]\s*([^:]+):\s?(.*)$",
    re.IGNORECASE,
)


def parse_messages(chat_log):
    """
    Turns raw copied WhatsApp text into a list of (sender, message) tuples. Lines that don't start a new "[timestamp] Sender:" block are treated as a continuation of the previous message (WhatsApp wraps long messages, and copy-paste preserves those as separate physical lines).

    [6:37 am, 12/7/2026] Anshu: Hello! --> (Anshu, Hello!)
    """
    messages = []
    for raw_line in chat_log.strip().splitlines():
        line = raw_line.strip()
        if not line:
            continue

        match = MESSAGE_LINE_RE.match(line)
        if match:
            sender, content = match.group(1).strip(), match.group(2).strip()
            messages.append([sender, content])
        else:
            # Continuation of the previous message (no new timestamp/sender)
            if messages:
                messages[-1][1] = (messages[-1][1] + " " + line).strip()
            # if there's no previous message yet, silently drop stray line

    return [(sender, content) for sender, content in messages]


def _normalize_sender(name):
    """Strips emoji/symbols so 'Yash 👒' matches 'Yash', case-insensitively."""
    
    cleaned = re.sub(r"[^\w\s]", "", name, flags=re.UNICODE).strip()
    return cleaned.lower()


def is_last_message_from_sender(chat_log, sender_name="Anshu"):
    messages = parse_messages(chat_log)
    if not messages:
        return False

    last_sender, _ = messages[-1]
    return _normalize_sender(last_sender) == _normalize_sender(sender_name)


def ai_process(chat_history):
    """Sends chat history to Gemini and returns the generated reply text."""
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",  # Replace with your preferred valid model
        contents=chat_history,
        config=genai.types.GenerateContentConfig(
            system_instruction=(
                "You're a person named Yash who speaks Marathi, Hindi, and English. "
                "You're from India and you're a coder. "
                "Analyze the chat history and output only the next reply as Yash. "
                "Return only the message text. Do not include quotes, explanations, or markdown."
            )
        ),
    )
    return response.text


def main():
    # Step 1: Click on the Chrome icon
    pyautogui.click(1247, 1045)
    time.sleep(2)  # Wait to ensure the click is registered

    while True:
        if keyboard.is_pressed("esc"):
            print("Exiting...")
            break

        # Step 2: Drag the mouse to select the chat text
        pyautogui.moveTo(680, 205)
        pyautogui.dragTo(1883, 926, duration=2.0, button="left")

        # Step 3: Copy the selected text to the clipboard
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)  # Wait to ensure the copy command completes
        pyautogui.click(680, 205)  # Deselect

        # Step 4: Retrieve the text from the clipboard
        chat_history = pyperclip.paste()

        print("=" * 50)
        print(chat_history)
        print("=" * 50)

        if is_last_message_from_sender(chat_history):
            print("New message from Anshu detected.")

            reply = ai_process(chat_history)
            print("Reply: ", reply)

            pyperclip.copy(reply)

            # Step 5: Click on the message input field
            pyautogui.click(1210, 976)
            time.sleep(1)  # Wait to ensure the click is registered

            # Step 6: Paste the reply
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)  # Wait to ensure the paste command completes

            # Step 7: Press Enter
            pyautogui.press("enter")


if __name__ == "__main__":
    main()