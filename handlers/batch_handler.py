from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.command_handler import CommandHandler
from database.file_manager import FileManager
from config import AUTO_DELETE_ENABLED, AUTO_DELETE_TIMER
import asyncio

batch_states = {}

@filters.command("batch")
@CommandHandler.ban_check
@CommandHandler.force_sub_check
async def batch_handler(client: Client, message):
    user_id = message.from_user.id
    await message.reply("How many files do you want to upload? Please enter a number (e.g., 1, 2, 3...)")
    batch_states[user_id] = {"step": "awaiting_count"}

@filters.regex(r"^\d+$")
@CommandHandler.ban_check
async def batch_count_handler(client: Client, message):
    user_id = message.from_user.id
    if user_id not in batch_states or batch_states[user_id]["step"] != "awaiting_count":
        return

    count = int(message.text)
    batch_states[user_id] = {"step": "collecting_files", "count": count, "files": [], "current": 0}
    await message.reply(f"Please upload {count} files one by one.")

@filters.document
@CommandHandler.ban_check
async def batch_file_handler(client: Client, message):
    user_id = message.from_user.id
    if user_id not in batch_states or batch_states[user_id]["step"] != "collecting_files":
        return

    state = batch_states[user_id]
    state["files"].append(message.document.file_id)
    state["current"] += 1

    if state["current"] < state["count"]:
        await message.reply(f"File {state['current']} uploaded. Please upload the next file.")
        return

    # All files collected, generate share link
    share_links = []
    for file_id in state["files"]:
        share_link = await FileManager.add_file(file_id, "document")
        share_links.append(share_link)

    combined_link = "_".join(share_links)
    share_url = f"https://t.me/{client.me.username}?start=batch_{combined_link}"
    buttons = [[InlineKeyboardButton("Share Link", url=share_url)]]
    msg = await message.reply(
        f"Here is your batch share link:\n{share_url}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    # Auto-delete logic
    if AUTO_DELETE_ENABLED:
        await message.reply(f"This batch will be deleted in {AUTO_DELETE_TIMER // 60} minutes. Forward it to save!")
        await asyncio.sleep(AUTO_DELETE_TIMER)
        await msg.delete()
        await message.reply("Batch deleted.")

    # Clean up state
    del batch_states[user_id]
