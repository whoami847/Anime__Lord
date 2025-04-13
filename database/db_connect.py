from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import MONGO_URI, DB_NAME, LOG_LEVEL  # LOG_LEVEL ইমপোর্ট করা হলো
import logging

# Configure logging
logging.basicConfig(level=getattr(logging, LOG_LEVEL))
logger = logging.getLogger(__name__)

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            try:
                cls._instance.client = MongoClient(
                    MONGO_URI,
                    maxPoolSize=50,  # Advanced connection pooling
                    connectTimeoutMS=10000,
                    serverSelectionTimeoutMS=10000
                )
                cls._instance.db = cls._instance.client[DB_NAME]
                logger.info("Database connection established successfully.")
            except ConnectionFailure as e:
                logger.error(f"Failed to connect to MongoDB: {e}")
                raise
        return cls._instance

    @property
    def connection(self):
        return self.db

# Singleton instance
db = Database().connection
