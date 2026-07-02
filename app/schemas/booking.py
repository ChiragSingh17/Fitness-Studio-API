"""Booking schemas"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class BookingCreate(BaseModel):
    """Create booking schema"""
    class_id: str = Field(..., alias="classId")
    client_name: str = Field(..., min_length=1, max_length=100, alias="clientName")
    client_email: EmailStr = Field(..., alias="clientEmail")
    
    class Config:
        populate_by_name = True


class BookingResponse(BaseModel):
    """Booking response schema"""
    id: str = Field(alias="_id")
    class_id: str = Field(alias="classId")
    client_name: str = Field(alias="clientName")
    client_email: str = Field(alias="clientEmail")
    created_at: datetime = Field(alias="createdAt")
    
    class Config:
        populate_by_name = True
