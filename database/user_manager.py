from database.db_connect import get_db
import logging

logger = logging.getLogger(__name__)

class UserManager:
    @staticmethod
    async def add_user(user_id, username):
        db = get_db()
        users = db.users
        user = {"user_id": user_id, "username": username, "banned": False}
        await users.insert_one(user)
        logger.debug(f"User {user_id} added to database.")

    @staticmethod
    async def ban_user(user_id, reason):
        db = get_db()
        users = db.users
        await users.update_one({"user_id": user_id}, {"$set": {"banned": True, "ban_reason": reason}})
        logger.info(f"User {user_id} banned. Reason: {reason}")

    @staticmethod
    async def unban_user(user_id):
        db = get_db()
        users = db.users
        await users.update_one({"user_id": user_id}, {"$set": {"banned": False}})
        logger.info(f"User {user_id} unbanned.")

    @staticmethod
    async def get_all_users():
        db = get_db()
        users = db.users
        return await users.find().to_list(None)
