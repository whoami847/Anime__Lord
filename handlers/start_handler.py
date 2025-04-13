from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import WELCOME_MESSAGE, WELCOME_IMAGES_DIR, FORCE_SUB_CHANNELS
from utils.message_formatter import MessageFormatter
from database.user_manager import UserManager

@filters.command("start")
async def start_handler(client: Client, message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Add user to database
    await UserManager.add_user(user_id, username)

    # Check force sub
    if FORCE_SUB_CHANNELS:
        for channel in FORCE_SUB_CHANNELS:
            try:
                member = await client.get_chat_member(channel, user_id)
                if member.status == "left":
                    await message.reply(f"Please join {channel} to use this bot!")
                    return
            except Exception:
                await message.reply(f"Please join {channel} to use this bot!")
                return

    # Format welcome message
    text, image = MessageFormatter.format_message(WELCOME_MESSAGE, WELCOME_IMAGES_DIR)
    buttons = [
        [InlineKeyboardButton("About", callback_data="about"), InlineKeyboardButton("Settings", callback_data="settings")]
    ]
    await message.reply_photo(
        photo=image,
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons)
      )
