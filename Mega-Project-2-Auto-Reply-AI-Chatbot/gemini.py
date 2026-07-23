from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Gemini AI Client processing command
client = genai.Client(api_key=gemini_api_key)

def aiProcess(command):

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=command,


        config=genai.types.GenerateContentConfig(
            system_instruction=(
                "You're a person named Yash who speaks Marathi, Hindi as well as English. He is from India and is a coder. You analyze chat history and respond like Yash."
            )
        ),
    )

    return response.text