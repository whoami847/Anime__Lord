from pyrogram import Client
from utils.command_handler import CommandHandler
import os
import sys
import logging

logger = logging.getLogger(__name__)

async def restart_handler(client: Client, message):
    await message.reply("Restarting the bot...")
    logger.info("Bot restart initiated by admin.")
    os.execv(sys.executable, ['python'] + sys.argv)
