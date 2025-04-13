from pyrogram import Client
from utils.command_handler import CommandHandler
from config import WELCOME_MESSAGE, WELCOME_IMAGES_DIR
import os

async def welcome_edit_handler(client: Client, message):
    if len(message.command) < 2:
        await message.reply(f"Current welcome message:\n{WELCOME_MESSAGE}\n\nPlease provide a new message (e.g., /welcome_edit New message here)")
        return

    new_message = " ".join(message.command[1:])
    with open("config.py", "r") as f:
        lines = f.readlines()

    with open("config.py", "w") as f:
        for line in lines:
            if line.startswith("WELCOME_MESSAGE"):
                f.write(f'WELCOME_MESSAGE = "{new_message}"\n')
            else:
                f.write(line)

    await message.reply(f"Welcome message updated to:\n{new_message}")

async def welcome_edit_img_handler(client: Client, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply("Please reply to a photo to set as the welcome image!")
        return

    photo = message.reply_to_message.photo
    file_path = os.path.join(WELCOME_IMAGES_DIR, f"welcome_image_{photo.file_id}.jpg")
    await photo.download(file_path)
    await message.reply("Welcome image updated successfully!")
