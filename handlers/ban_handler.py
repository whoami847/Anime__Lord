from pyrogram import Client
from utils.command_handler import CommandHandler
from database.user_manager import UserManager

async def ban_handler(client: Client, message):
    if not message.reply_to_message:
        await message.reply("Please reply to a user's message to ban them!")
        return

    user_id = message.reply_to_message.from_user.id
    reason = " ".join(message.command[1:]) if len(message.command) > 1 else "No reason provided"
    await UserManager.ban_user(user_id, reason)
    await message.reply(f"User {user_id} has been banned. Reason: {reason}")
    await client.send_message(user_id, f"You have been banned from the bot. Reason: {reason}")

async def unban_handler(client: Client, message):
    if not message.reply_to_message:
        await message.reply("Please reply to a user's message to unban them!")
        return

    user_id = message.reply_to_message.from_user.id
    await UserManager.unban_user(user_id)
    await message.reply(f"User {user_id} has been unbanned.")
    await client.send_message(user_id, "You have been unbanned from the bot.")
