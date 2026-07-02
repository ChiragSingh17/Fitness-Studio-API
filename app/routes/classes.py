"""Fitness Class routes"""
from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.fitness_class import ClassCreate, ClassResponse
from app.utils.dependencies import get_current_user
from app.utils.timezone import convert_to_utc
from app.database import get_database
from bson import ObjectId
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/classes", tags=["classes"])


@router.post("", response_model=ClassResponse, status_code=status.HTTP_201_CREATED)
async def create_class(
    class_data: ClassCreate,
    current_user: dict = Depends(get_current_user)
):
    """
    Create a new fitness class
    
    Requires authentication. Only authenticated users can create classes.
    
    - **name**: Class name (e.g., "Yoga Flow")
    - **dateTime**: Class date and time in ISO format (e.g., "2025-06-15T10:00:00Z")
    - **instructor**: Instructor name
    - **availableSlots**: Number of available slots (must be > 0)
    """
    db = get_database()
    
    # Validate that class date is in future
    if class_data.dateTime <= datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Class date must be in the future"
        )
    
    # Create class document
    class_doc = {
        "name": class_data.name,
        "date_time": class_data.dateTime,
        "instructor": class_data.instructor,
        "available_slots": class_data.availableSlots,
        "booked_slots": 0,
        "created_by": current_user["user_id"],
        "created_at": datetime.utcnow(),
    }
    
    try:
        result = db.fitness_classes.insert_one(class_doc)
        class_doc["_id"] = result.inserted_id
        
        logger.info(f"Class created successfully: {class_data.name}")
        return ClassResponse(**class_doc)
    
    except Exception as e:
        logger.error(f"Error creating class: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create class"
        )


@router.get("", response_model=list[ClassResponse])
async def get_classes():
    """
    Fetch all upcoming fitness classes
    
    Returns all classes with future dates, sorted by date.
    """
    db = get_database()
    
    try:
        # Get all classes with future dates
        classes = list(db.fitness_classes.find(
            {"date_time": {"$gt": datetime.utcnow()}}
        ).sort("date_time", 1))
        
        logger.info(f"Retrieved {len(classes)} upcoming classes")
        return [ClassResponse(**cls) for cls in classes]
    
    except Exception as e:
        logger.error(f"Error fetching classes: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch classes"
        )
