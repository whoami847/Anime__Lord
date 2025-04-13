from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, DB_NAME
import logging

logger = logging.getLogger(__name__)

client = None
db = None

async def connect_to_db():
    global client, db
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[DB_NAME]
        logger.info("Database connection established successfully.")
    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")
        raise

async def get_db():
    global db
    if db is None:
        await connect_to_db()
    return db

async def close_db():
    global client
    if client:
        client.close()
        logger.info("Database connection closed.")
