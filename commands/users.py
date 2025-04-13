from database.user_manager import UserManager

async def users_list(limit: int = 10, offset: int = 0):
    users = await UserManager.get_all_users(limit, offset)
    text = "Users List:\n"
    for user in users:
        text += f"ID: {user['user_id']} | Username: {user.get('username', 'N/A')} | Banned: {user.get('banned', False)}\n"
    return text
