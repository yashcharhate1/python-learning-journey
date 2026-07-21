import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import requests
import musicLibrary
import pywhatkit
from google import genai
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

# Mixer is initialized once at import time, not on every speak() call
pygame.mixer.init()


def speak_old(text):
    engine = pyttsx3.init("sapi5")
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    # Load the mp3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# Gemini AI Client processing command
client = genai.Client(api_key=gemini_api_key)

def aiProcess(command):

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=command,


        config=genai.types.GenerateContentConfig(
            system_instruction=(
                "You're a virtual assistant named Narad skilled in general tasks "
                "like Alexa and ChatGPT. Give short responses please."
            )
        ),
    )

    return response.text


def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        # Everything after "play " is the song name, not just the 2nd word,
        # so multi-word titles like "play beauty and a beat" work.
        song = c[len("play"):].strip().lower()

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            # Not in the local library -> fall back to searching YouTube directly
            speak(f"I don't have {song} saved, searching YouTube instead.")
            try:
                pywhatkit.playonyt(song)
            except Exception:
                speak("Sorry, I couldn't play that.")

    elif "news" in c.lower():
        if not news_api_key:
            speak("I don't have a news API key configured.")
        else:
            try:
                r = requests.get(
                    "https://newsapi.org/v2/top-headlines",
                    params={
                        "country": "us",
                        "apiKey": news_api_key
                    },
                    timeout=10
                )
                r.raise_for_status()
                data = r.json()
                articles = data.get("articles", [])

                if not articles:
                    speak("I couldn't find any news right now.")
                else:
                    # Read out a handful of headlines in a single utterance
                    # instead of one speak() call (one gTTS round-trip) per article.
                    top_titles = [a["title"] for a in articles[:5] if a.get("title")]
                    headline_text = "Here are the top headlines. " + ". ".join(top_titles)
                    speak(headline_text)

            except requests.RequestException as e:
                print(f"News request failed: {e}")
                speak("Sorry, I couldn't fetch the news right now.")

    else:
        # Let Gemini AI Handled the Request
        output = aiProcess(c)
        print(output)
        speak(output)


    # elif c.lower().startswith("play"):
    #     song = c[5:].strip()  # Everything after "play "
    #     speak(f"Playing {song}")
    #     webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    #     pywhatkit.playonyt(song)



if __name__ == "__main__":
    speak("Initializing Devarshi Narad.....")
    while True:


        # recognize speech using Google
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, phrase_time_limit=6)

            print("Recognizing....")

            word = r.recognize_google(audio)
            print(word)
            if any(wake in word.lower() for wake in ["sia", "narayana", "narayan", "meera", "narayana narayana"]):
                time.sleep(0.2)
                speak("Narayana Narayana")

                # Listen for command
                with sr.Microphone() as source:
                    print(" Narad Active ...")
                    audio = r.listen(source, phrase_time_limit=8)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))