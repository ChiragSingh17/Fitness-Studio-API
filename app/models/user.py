"""User model"""
from typing import Optional
from datetime import datetime
from bson import ObjectId


class User:
    """User database model"""
    
    def __init__(
        self,
        name: str,
        email: str,
        hashed_password: str,
        _id: Optional[ObjectId] = None,
        created_at: Optional[datetime] = None,
    ):
        self._id = _id or ObjectId()
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self) -> dict:
        """Convert user to dictionary"""
        return {
            "_id": self._id,
            "name": self.name,
            "email": self.email,
            "hashed_password": self.hashed_password,
            "created_at": self.created_at,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Create user from dictionary"""
        return cls(
            _id=data.get("_id"),
            name=data.get("name"),
            email=data.get("email"),
            hashed_password=data.get("hashed_password"),
            created_at=data.get("created_at"),
        )
