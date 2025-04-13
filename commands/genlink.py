from pyrogram import Client
from database.file_manager import FileManager
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def genlink(client: Client, message):
    file = message.reply_to_message.document
    file_id = file.file_id
    caption = message.reply_to_message.caption

    share_link = await FileManager.add_file(file_id, "document", caption)
    share_url = f"https://t.me/{client.me.username}?start=share_{share_link}"
    buttons = [[InlineKeyboardButton("Share Link", url=share_url)]]
    return share_url, InlineKeyboardMarkup(buttons)
