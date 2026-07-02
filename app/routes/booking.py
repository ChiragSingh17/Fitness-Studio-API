"""Booking routes"""
from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.booking import BookingCreate, BookingResponse
from app.utils.dependencies import get_current_user
from app.database import get_database
from bson import ObjectId
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def book_class(
    booking_data: BookingCreate,
    current_user: dict = Depends(get_current_user)
):
    """
    Book a slot in a fitness class
    
    Requires authentication.
    
    - **classId**: The ID of the class to book
    - **clientName**: Name of the client booking the class
    - **clientEmail**: Email of the client
    
    Validations:
    - Checks if class exists
    - Checks if slots are available
    - Prevents duplicate bookings for the same user
    - Prevents overbooking
    """
    db = get_database()
    
    try:
        # Validate and get class
        try:
            class_id = ObjectId(booking_data.class_id)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid class ID format"
            )
        
        fitness_class = db.fitness_classes.find_one({"_id": class_id})
        
        if not fitness_class:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Class not found"
            )
        
        # Check if slots are available
        if fitness_class["booked_slots"] >= fitness_class["available_slots"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No available slots for this class"
            )
        
        # Check if user already booked this class
        existing_booking = db.bookings.find_one({
            "class_id": class_id,
            "user_id": ObjectId(current_user["user_id"])
        })
        
        if existing_booking:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have already booked this class"
            )
        
        # Create booking document
        booking_doc = {
            "class_id": class_id,
            "user_id": ObjectId(current_user["user_id"]),
            "client_name": booking_data.client_name,
            "client_email": booking_data.client_email,
            "created_at": datetime.utcnow(),
        }
        
        # Insert booking and update available slots (atomic operation)
        result = db.bookings.insert_one(booking_doc)
        booking_doc["_id"] = result.inserted_id
        
        # Update class booked slots
        db.fitness_classes.update_one(
            {"_id": class_id},
            {"$inc": {"booked_slots": 1}}
        )
        
        logger.info(f"Booking created successfully for class {class_id}")
        return BookingResponse(**booking_doc)
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating booking: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create booking"
        )


@router.get("", response_model=list[BookingResponse])
async def get_user_bookings(
    current_user: dict = Depends(get_current_user)
):
    """
    Fetch all bookings for the authenticated user
    
    Returns a list of all classes booked by the current user.
    """
    db = get_database()
    
    try:
        bookings = list(db.bookings.find({
            "user_id": ObjectId(current_user["user_id"])
        }).sort("created_at", -1))
        
        logger.info(f"Retrieved {len(bookings)} bookings for user {current_user['user_id']}")
        return [BookingResponse(**booking) for booking in bookings]
    
    except Exception as e:
        logger.error(f"Error fetching bookings: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch bookings"
        )
