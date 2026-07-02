"""Seed data for testing and development"""
from datetime import datetime, timedelta
from app.database import get_database
from app.utils.auth import hash_password
import logging

logger = logging.getLogger(__name__)


def seed_users(db):
    """Seed sample users"""
    users = [
        {
            "name": "John Doe",
            "email": "john@example.com",
            "hashed_password": hash_password("password123"),
            "created_at": datetime.utcnow(),
        },
        {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "hashed_password": hash_password("password123"),
            "created_at": datetime.utcnow(),
        },
        {
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "hashed_password": hash_password("password123"),
            "created_at": datetime.utcnow(),
        },
    ]
    
    result = db.users.insert_many(users)
    logger.info(f"Inserted {len(result.inserted_ids)} users")
    return result.inserted_ids


def seed_classes(db, user_ids):
    """Seed sample fitness classes"""
    base_time = datetime.utcnow() + timedelta(days=1)
    
    classes = [
        {
            "name": "Yoga Flow",
            "date_time": base_time + timedelta(hours=8),
            "instructor": "John Doe",
            "available_slots": 20,
            "booked_slots": 0,
            "created_by": str(user_ids[0]),
            "created_at": datetime.utcnow(),
        },
        {
            "name": "HIIT Session",
            "date_time": base_time + timedelta(hours=10),
            "instructor": "Jane Smith",
            "available_slots": 15,
            "booked_slots": 0,
            "created_by": str(user_ids[0]),
            "created_at": datetime.utcnow(),
        },
        {
            "name": "Zumba Party",
            "date_time": base_time + timedelta(hours=18),
            "instructor": "Maria Garcia",
            "available_slots": 25,
            "booked_slots": 0,
            "created_by": str(user_ids[1]),
            "created_at": datetime.utcnow(),
        },
        {
            "name": "Pilates Core",
            "date_time": base_time + timedelta(hours=16),
            "instructor": "Emma Wilson",
            "available_slots": 12,
            "booked_slots": 0,
            "created_by": str(user_ids[1]),
            "created_at": datetime.utcnow(),
        },
        {
            "name": "Spinning Class",
            "date_time": base_time + timedelta(hours=6),
            "instructor": "Tom Anderson",
            "available_slots": 30,
            "booked_slots": 0,
            "created_by": str(user_ids[2]),
            "created_at": datetime.utcnow(),
        },
    ]
    
    result = db.fitness_classes.insert_many(classes)
    logger.info(f"Inserted {len(result.inserted_ids)} fitness classes")
    return result.inserted_ids


def seed_bookings(db, user_ids, class_ids):
    """Seed sample bookings"""
    bookings = [
        {
            "class_id": class_ids[0],
            "user_id": user_ids[1],
            "client_name": "Jane Smith",
            "client_email": "jane@example.com",
            "created_at": datetime.utcnow(),
        },
        {
            "class_id": class_ids[1],
            "user_id": user_ids[2],
            "client_name": "Alice Johnson",
            "client_email": "alice@example.com",
            "created_at": datetime.utcnow(),
        },
        {
            "class_id": class_ids[0],
            "user_id": user_ids[2],
            "client_name": "Alice Johnson",
            "client_email": "alice@example.com",
            "created_at": datetime.utcnow(),
        },
    ]
    
    result = db.bookings.insert_many(bookings)
    
    # Update booked slots
    for booking in bookings:
        db.fitness_classes.update_one(
            {"_id": booking["class_id"]},
            {"$inc": {"booked_slots": 1}}
        )
    
    logger.info(f"Inserted {len(result.inserted_ids)} bookings")
    return result.inserted_ids


def seed_database():
    """Seed the entire database"""
    from app.database import connect_to_mongo
    
    logger.info("Starting database seeding...")
    
    try:
        db = connect_to_mongo()
        
        # Clear existing data
        db.users.delete_many({})
        db.fitness_classes.delete_many({})
        db.bookings.delete_many({})
        logger.info("Cleared existing data")
        
        # Seed data
        user_ids = seed_users(db)
        class_ids = seed_classes(db, user_ids)
        seed_bookings(db, user_ids, class_ids)
        
        logger.info("Database seeding completed successfully")
        print("\n✅ Database seeded successfully!")
        print(f"Created {len(user_ids)} users")
        print(f"Created {len(class_ids)} fitness classes")
        
    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        raise


if __name__ == "__main__":
    seed_database()
