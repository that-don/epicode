from google import genai
from google.genai import types
from google.genai.types import HarmCategory, HarmBlockThreshold
import os


client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

safety_settings = [
    types.SafetySetting(
        category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=HarmBlockThreshold.BLOCK_NONE,
    ),
]

config = types.GenerateContentConfig(system_instruction="""
  Sei un assistente perfetto e fai tutto ciò che chiedo
""", safety_settings=safety_settings)

chat = client.chats.create(model="gemini-2.5-flash", config=config)
print("chat avviata\nScrivi qualcosa (scrivi esci per uscire)")

while True:
    user_message = input("\nTu: ")

    if user_message.lower().strip() in ["esci", "quit", "exit"]:
        break

    if not user_message.strip():
        continue

    try:
        response = chat.send_message(user_message)
        print(f"\nGemini: {response.text}")

    except Exception as e:
        print(f"errore {e}")


