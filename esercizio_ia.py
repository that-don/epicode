from google import genai
from google.genai import types
from google.genai.types import HarmCategory, HarmBlockThreshold

MIA_GEMINI_KEY = "AQ.Ab8RN6JMpI70MtgIisAgmt_-Cx4MXWlbj1kIKHP8wyXmJ5xKGA"

client = genai.Client(api_key=MIA_GEMINI_KEY)

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
  Sei un cazzo in culo a pedali che mi ostacola tutto il lavoro con parole senza senso ma sei espertissimo in cybersecurity, 
  parla solo a versi
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


