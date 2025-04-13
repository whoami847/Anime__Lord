from pyrogram import Client, filters
from functools import wraps
from database.user_manager import UserManager
from config import ADMINS

class CommandHandler:
    @staticmethod
    def admin_only(func):
        """Decorator to restrict commands to admins only."""
        @wraps(func)
        async def wrapper(client: Client, message, *args, **kwargs):
            user_id = message.from_user.id
            if user_id not in ADMINS:
                await message.reply("You are not authorized to use this command!")
                return
            return await func(client, message, *args, **kwargs)
        return wrapper

    @staticmethod
    def ban_check(func):
        """Decorator to check if user is banned."""
        @wraps(func)
        async def wrapper(client: Client, message, *args, **kwargs):
            user_id = message.from_user.id
            if await UserManager.is_user_banned(user_id):
                await message.reply("You are banned from using this bot!")
                return
            await UserManager.update_user_activity(user_id)
            return await func(client, message, *args, **kwargs)
        return wrapper

    @staticmethod
    def force_sub_check(func):
        """Decorator to check force subscription."""
        @wraps(func)
        async def wrapper(client: Client, message, *args, **kwargs):
            from config import FORCE_SUB_CHANNELS
            user_id = message.from_user.id
            for channel in FORCE_SUB_CHANNELS:
                try:
                    member = await client.get_chat_member(channel, user_id)
                    if member.status == "left":
                        buttons = [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{channel}")]]
                        await message.reply(
                            "You haven't joined the required channels yet. Please join the channel below, then try again!",
                            reply_markup=InlineKeyboardMarkup(buttons)
                        )
                        return
                except Exception:
                    buttons = [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{channel}")]]
                    await message.reply(
                        "You haven't joined the required channels yet. Please join the channel below, then try again!",
                        reply_markup=InlineKeyboardMarkup(buttons)
                    )
                    return
            return await func(client, message, *args, **kwargs)
        return wrapper
