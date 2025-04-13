from pyrogram import Client, filters
from utils.command_handler import CommandHandler
from database.user_manager import UserManager
from utils.message_formatter import MessageFormatter
import asyncio

@filters.command("broadcast")
@CommandHandler.admin_only
async def broadcast_handler(client: Client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a message to broadcast!")
        return

    broadcast_msg = " ".join(message.command[1:])
    formatted_msg, _ = MessageFormatter.format_message(broadcast_msg)

    users = await UserManager.get_all_users()
    success_count = 0
    failed_count = 0

    for user in users:
        try:
            await client.send_message(user["user_id"], formatted_msg)
            success_count += 1
            await asyncio.sleep(0.1)  # Rate limiting
        except Exception:
            failed_count += 1

    await message.reply(f"Broadcast completed!\nSuccess: {success_count}\nFailed: {failed_count}")
