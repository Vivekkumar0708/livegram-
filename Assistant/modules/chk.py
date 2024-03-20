import requests
from pyrogram import Client, filters
import random
from Assistant import Abishnoi as app
from config import TOKEN
from pyrogram.types import Message

# Define the URL to send the message reaction
url = f"https://api.telegram.org/bot{TOKEN}/setMessageReaction"

# Define the function to send the message reaction
def send_reaction(chat_id, message_id, emoji):
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [{"type": "emoji", "emoji": emoji, "is_big": True}]
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Reaction sent successfully!")
    else:
        print(f"Failed to send reaction. Status code: {response.status_code}")

# Define your handler
@app.on_message(filters.private)
def handle_message(client, message: Message):
    # Get the chat ID and message ID directly from the message object
    chat_id = message.chat.id
    message_id = message.message_id.message_id
    # Select a random emoji
    do_emoji = random.choice(["👍", "👎", "❤", "🔥", "🥰"])
    # Call the function to send the message reaction
    send_reaction(chat_id, message_id, do_emoji)