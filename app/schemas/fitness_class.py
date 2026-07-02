"""Fitness Class schemas"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ClassCreate(BaseModel):
    """Create fitness class schema"""
    name: str = Field(..., min_length=1, max_length=100)
    dateTime: datetime
    instructor: str = Field(..., min_length=1, max_length=100)
    availableSlots: int = Field(..., gt=0)


class ClassUpdate(BaseModel):
    """Update fitness class schema"""
    name: Optional[str] = None
    instructor: Optional[str] = None
    available_slots: Optional[int] = None


class ClassResponse(BaseModel):
    """Fitness class response schema"""
    id: str = Field(alias="_id")
    name: str
    dateTime: datetime = Field(alias="date_time")
    instructor: str
    availableSlots: int = Field(alias="available_slots")
    bookedSlots: int = Field(default=0, alias="booked_slots")
    createdBy: str = Field(alias="created_by")
    createdAt: datetime = Field(alias="created_at")
    
    class Config:
        populate_by_name = True
