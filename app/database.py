"""MongoDB database connection and utilities"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from app.config import settings
import logging

logger = logging.getLogger(__name__)

client: MongoClient = None
db = None


def connect_to_mongo():
    """Connect to MongoDB"""
    global client, db
    try:
        client = MongoClient(settings.MONGODB_URL)
        db = client[settings.DATABASE_NAME]
        # Verify connection
        client.admin.command('ping')
        logger.info("Connected to MongoDB successfully")
        return db
    except ConnectionFailure as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise


def close_mongo_connection():
    """Close MongoDB connection"""
    global client
    if client is not None:
        client.close()
        logger.info("MongoDB connection closed")


def get_database():
    """Get database instance"""
    return db
