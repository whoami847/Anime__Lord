from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.message_formatter import MessageFormatter
from utils.command_handler import CommandHandler
from config import ABOUT_MESSAGE

async def help_handler(client: Client, message):
    text, _ = MessageFormatter.format_message(
        f"{ABOUT_MESSAGE}\n\nSTILL HAVE DOUBTS, CONTACT BELOW PERSONS/GROUP AS PER YOUR NEED!"
    )
    buttons = [
        [InlineKeyboardButton("Support Chat Group", url="https://t.me/support_chat_group")],
        [InlineKeyboardButton("Owner", url="https://t.me/owner_username")],
        [InlineKeyboardButton("Developer", url="https://t.me/shidoteshika1")]
    ]
    await message.reply(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
