from .db_connect import db
import uuid
from datetime import datetime, timedelta

files_collection = db["files"]

class FileManager:
    @staticmethod
    async def add_file(file_id: str, file_type: str, caption: str = None, expiry_days: int = 7):
        """Add a file with metadata and expiry."""
        share_link = str(uuid.uuid4())
        expiry_date = datetime.utcnow() + timedelta(days=expiry_days)
        file_data = {
            "file_id": file_id,
            "file_type": file_type,
            "caption": caption,
            "share_link": share_link,
            "created_at": datetime.utcnow(),
            "expires_at": expiry_date,
            "access_count": 0
        }
        files_collection.insert_one(file_data)
        return share_link

    @staticmethod
    async def get_file_by_link(share_link: str):
        """Get file by share link with expiry check."""
        file = files_collection.find_one({"share_link": share_link})
        if file and file["expires_at"] < datetime.utcnow():
            files_collection.delete_one({"share_link": share_link})
            return None
        if file:
            files_collection.update_one(
                {"share_link": share_link},
                {"$inc": {"access_count": 1}}
            )
        return file

    @staticmethod
    async def cleanup_expired_files():
        """Remove expired files from the database."""
        files_collection.delete_many({"expires_at": {"$lt": datetime.utcnow()}})
