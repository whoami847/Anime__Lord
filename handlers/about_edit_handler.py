from pyrogram import Client, filters
from utils.command_handler import CommandHandler
from config import ABOUT_MESSAGE, ABOUT_IMAGES_DIR
import os

@filters.command("about_edit_msg")
@CommandHandler.admin_only
async def about_edit_msg_handler(client: Client, message):
    if len(message.command) < 2:
        await message.reply(f"Current about message:\n{ABOUT_MESSAGE}\n\nPlease provide a new message (e.g., /about_edit_msg New message here)")
        return

    new_message = " ".join(message.command[1:])
    with open("config.py", "r") as f:
        lines = f.readlines()

    with open("config.py", "w") as f:
        for line in lines:
            if line.startswith("ABOUT_MESSAGE"):
                f.write(f'ABOUT_MESSAGE = "{new_message}"\n')
            else:
                f.write(line)

    await message.reply(f"About message updated to:\n{new_message}")

@filters.command("about_edit_img")
@CommandHandler.admin_only
async def about_edit_img_handler(client: Client, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply("Please reply to a photo to set as the about image!")
        return

    photo = message.reply_to_message.photo
    file_path = os.path.join(ABOUT_IMAGES_DIR, f"about_image_{photo.file_id}.jpg")
    await photo.download(file_path)
    await message.reply("About image updated successfully!")
