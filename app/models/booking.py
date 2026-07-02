"""Booking model"""
from typing import Optional
from datetime import datetime
from bson import ObjectId


class Booking:
    """Booking database model"""
    
    def __init__(
        self,
        class_id: ObjectId,
        user_id: ObjectId,
        client_name: str,
        client_email: str,
        _id: Optional[ObjectId] = None,
        created_at: Optional[datetime] = None,
    ):
        self._id = _id or ObjectId()
        self.class_id = class_id
        self.user_id = user_id
        self.client_name = client_name
        self.client_email = client_email
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self) -> dict:
        """Convert booking to dictionary"""
        return {
            "_id": self._id,
            "class_id": self.class_id,
            "user_id": self.user_id,
            "client_name": self.client_name,
            "client_email": self.client_email,
            "created_at": self.created_at,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Booking":
        """Create booking from dictionary"""
        return cls(
            _id=data.get("_id"),
            class_id=data.get("class_id"),
            user_id=data.get("user_id"),
            client_name=data.get("client_name"),
            client_email=data.get("client_email"),
            created_at=data.get("created_at"),
        )
