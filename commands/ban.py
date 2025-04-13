from database.user_manager import UserManager

async def ban_user(user_id: int, reason: str = None):
    await UserManager.ban_user(user_id, reason)
    return f"User {user_id} has been banned. Reason: {reason}"
