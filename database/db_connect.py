from pymongo import MongoClient
from config import MONGO_URI, DB_NAME
import logging

logger = logging.getLogger(__name__)

client = None
db = None

def connect_to_db():
    global client, db
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        logger.info("Database connection established successfully.")
    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")
        raise

def get_db():
    if db is None:
        connect_to_db()
    return db

def close_db():
    global client
    if client:
        client.close()
        logger.info("Database connection closed.")
