"""Fitness Class model"""
from typing import Optional
from datetime import datetime
from bson import ObjectId


class FitnessClass:
    """Fitness Class database model"""
    
    def __init__(
        self,
        name: str,
        date_time: datetime,
        instructor: str,
        available_slots: int,
        created_by: str,
        _id: Optional[ObjectId] = None,
        booked_slots: int = 0,
        created_at: Optional[datetime] = None,
    ):
        self._id = _id or ObjectId()
        self.name = name
        self.date_time = date_time
        self.instructor = instructor
        self.available_slots = available_slots
        self.booked_slots = booked_slots
        self.created_by = created_by
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self) -> dict:
        """Convert class to dictionary"""
        return {
            "_id": self._id,
            "name": self.name,
            "date_time": self.date_time,
            "instructor": self.instructor,
            "available_slots": self.available_slots,
            "booked_slots": self.booked_slots,
            "created_by": self.created_by,
            "created_at": self.created_at,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "FitnessClass":
        """Create class from dictionary"""
        return cls(
            _id=data.get("_id"),
            name=data.get("name"),
            date_time=data.get("date_time"),
            instructor=data.get("instructor"),
            available_slots=data.get("available_slots"),
            booked_slots=data.get("booked_slots", 0),
            created_by=data.get("created_by"),
            created_at=data.get("created_at"),
        )
