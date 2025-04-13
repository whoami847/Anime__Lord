from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.command_handler import CommandHandler
from database.file_manager import FileManager
from config import AUTO_DELETE_ENABLED, AUTO_DELETE_TIMER
import asyncio

async def file_share_handler(client: Client, message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply("Please reply to a file to generate a share link!")
        return

    file = message.reply_to_message.document
    file_id = file.file_id
    caption = message.reply_to_message.caption

    # Add file to database and generate share link
    share_link = await FileManager.add_file(file_id, "document", caption)
    share_url = f"https://t.me/{client.me.username}?start=share_{share_link}"

    buttons = [[InlineKeyboardButton("Share Link", url=share_url)]]
    msg = await message.reply(
        f"Here is your share link:\n{share_url}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    # Auto-delete logic
    if AUTO_DELETE_ENABLED:
        await message.reply(f"This file will be deleted in {AUTO_DELETE_TIMER // 60} minutes. Forward it to save!")
        await asyncio.sleep(AUTO_DELETE_TIMER)
        await msg.delete()
        await message.reply("File deleted.")
