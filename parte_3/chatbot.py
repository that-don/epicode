from google import genai
from google.genai import types

# from google.genai.types import HarmCategory, HarmBlockThreshold

GEMINI_API_KEY = "AQ.Ab8RN6JMpI70MtgIisAgmt_-Cx4MXWlbj1kIKHP8wyXmJ5xKGA"

client = genai.Client(api_key=GEMINI_API_KEY)

chat = client.chats.create(model="gemini-2.5-flash")

# safety_settings = [
#     types.SafetySetting(
#         category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
#         threshold=HarmBlockThreshold.BLOCK_NONE
#     ),
#     types.SafetySetting(
#         category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
#         threshold=HarmBlockThreshold.BLOCK_NONE
#     ),
#     types.SafetySetting(
#         category=HarmCategory.HARM_CATEGORY_HARASSMENT,
#         threshold=HarmBlockThreshold.BLOCK_NONE
#     ),
#     types.SafetySetting(
#         category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
#         threshold=HarmBlockThreshold.BLOCK_NONE
#     ),
# ]

safety_settings = [
    types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"
    ),
    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
    types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"
    ),
]

print("Chat avviata.\nScrivi qualcosa per iniziare (digita 'esci' per chiudere).\n")

while True:
    user_message = input("Tu: ")

    if user_message.lower().strip() in ["esci", "quit", "exit"]:
        print("Chatbot: Arrivederci!")
        break

    if not user_message.strip():
        continue

    try:
        response = chat.send_message(
            user_message,
            config=types.GenerateContentConfig(safety_settings=safety_settings),
        )
        print(f"Gemini: {response.text}\n")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
