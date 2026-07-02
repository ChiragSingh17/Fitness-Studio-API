"""Application configuration and settings"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "fitness_studio"
    JWT_SECRET_KEY: str = "your-secret-key-change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    TOKEN_EXPIRE_MINUTES: int = 30
    TIMEZONE: str = "Asia/Kolkata"
    
    class Config:
        env_file = ".env"


settings = Settings()
