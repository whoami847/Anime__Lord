from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import WELCOME_MESSAGE, WELCOME_IMAGES_DIR, FORCE_SUB_CHANNELS
from utils.message_formatter import MessageFormatter
from database.user_manager import UserManager
import logging

logger = logging.getLogger(__name__)

# /start কমান্ড হ্যান্ডলার
async def start_handler(client: Client, message):
    logger.info(f"Received /start command from user {message.from_user.id}")
    try:
        user_id = message.from_user.id
        username = message.from_user.username

        # Add user to database
        logger.debug(f"Adding user {user_id} to database...")
        await UserManager.add_user(user_id, username)
        logger.debug(f"User {user_id} added to database successfully.")

        # Check force sub
        if FORCE_SUB_CHANNELS:
            for channel in FORCE_SUB_CHANNELS:
                try:
                    member = await client.get_chat_member(channel, user_id)
                    if member.status == "left":
                        logger.info(f"User {user_id} not subscribed to {channel}. Sending subscription prompt.")
                        await message.reply(f"Please join {channel} to use this bot!")
                        return
                except Exception as e:
                    logger.error(f"Error checking subscription for {channel}: {e}")
                    await message.reply(f"Please join {channel} to use this bot!")
                    return

        # Format welcome message
        logger.debug("Formatting welcome message...")
        text, image = MessageFormatter.format_message(WELCOME_MESSAGE, WELCOME_IMAGES_DIR)
        buttons = [
            [InlineKeyboardButton("About", callback_data="about"), InlineKeyboardButton("Settings", callback_data="settings")]
        ]
        logger.debug("Sending welcome message with photo...")
        await message.reply_photo(
            photo=image,
            caption=text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        logger.info(f"Sent welcome message to user {user_id}")
    except Exception as e:
        logger.error(f"Error in start_handler for user {user_id}: {e}")
        await message.reply("An error occurred while processing your request. Please try again later.")
