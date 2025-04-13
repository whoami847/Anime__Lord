from database.user_manager import UserManager

async def unban_user(user_id: int):
    await UserManager.unban_user(user_id)
    return f"User {user_id} has been unbanned."
