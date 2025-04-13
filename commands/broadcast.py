from database.user_manager import UserManager

async def broadcast_message(client: Client, message: str):
    users = await UserManager.get_all_users()
    success_count = 0
    failed_count = 0

    for user in users:
        try:
            await client.send_message(user["user_id"], message)
            success_count += 1
        except Exception:
            failed_count += 1

    return success_count, failed_count
