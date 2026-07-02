"""Authentication routes"""
from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserSignUp, UserLogin, TokenResponse, UserResponse
from app.utils.auth import hash_password, verify_password, create_access_token
from app.database import get_database
from bson import ObjectId
import logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["auth"])


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserSignUp):
    """
    Register a new user
    
    - **name**: User's full name
    - **email**: User's email (must be unique)
    - **password**: User's password (min 6 characters)
    """
    db = get_database()
    
    # Check if user already exists
    existing_user = db.users.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash password
    hashed_password = hash_password(user_data.password)
    
    # Create user document
    user_doc = {
        "name": user_data.name,
        "email": user_data.email,
        "hashed_password": hashed_password,
        "created_at": ObjectId().generation_time,
    }
    
    try:
        result = db.users.insert_one(user_doc)
        user_doc["_id"] = result.inserted_id
        
        logger.info(f"User registered successfully: {user_data.email}")
        return UserResponse(**user_doc)
    
    except Exception as e:
        logger.error(f"Error registering user: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to register user"
        )


@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin):
    """
    Authenticate user and return JWT token
    
    - **email**: User's email
    - **password**: User's password
    """
    db = get_database()
    
    # Find user by email
    user = db.users.find_one({"email": credentials.email})
    
    if not user or not verify_password(credentials.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Create JWT token
    try:
        token, expires_in = create_access_token(
            user_id=str(user["_id"]),
            email=user["email"]
        )
        
        logger.info(f"User logged in successfully: {credentials.email}")
        return TokenResponse(
            access_token=token,
            expires_in=expires_in
        )
    
    except Exception as e:
        logger.error(f"Error generating token: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate token"
        )
