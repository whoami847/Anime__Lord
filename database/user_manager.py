from .db_connect import db
from datetime import datetime

users_collection = db["users"]

class UserManager:
    @staticmethod
    async def add_user(user_id: int, username: str = None):
        """Add a new user with additional metadata."""
        if not users_collection.find_one({"user_id": user_id}):
            user_data = {
                "user_id": user_id,
                "username": username,
                "banned": False,
                "join_date": datetime.utcnow(),
                "last_active": datetime.utcnow(),
                "file_requests": 0
            }
            users_collection.insert_one(user_data)
            return True
        return False

    @staticmethod
    async def ban_user(user_id: int, reason: str = None):
        """Ban a user with a reason."""
        users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"banned": True, "ban_reason": reason, "ban_date": datetime.utcnow()}}
        )

    @staticmethod
    async def unban_user(user_id: int):
        """Unban a user and clear ban data."""
        users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"banned": False, "ban_reason": None, "ban_date": None}}
        )

    @staticmethod
    async def is_user_banned(user_id: int) -> bool:
        """Check if a user is banned."""
        user = users_collection.find_one({"user_id": user_id})
        return user.get("banned", False) if user else False

    @staticmethod
    async def update_user_activity(user_id: int):
        """Update user's last active time and request count."""
        users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"last_active": datetime.utcnow()}, "$inc": {"file_requests": 1}}
        )

    @staticmethod
    async def get_all_users(limit: int = 1000, offset: int = 0):
        """Get all users with pagination."""
        return list(users_collection.find({}).skip(offset).limit(limit))
