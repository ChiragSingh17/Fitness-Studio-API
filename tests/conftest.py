"""Test configuration and fixtures"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app
from app.utils.auth import create_access_token
from datetime import datetime, timedelta


@pytest.fixture(autouse=True)
def mock_database():
    """Mock database globally for all tests"""
    with patch("app.database.db") as mock_db:
        # Create a mock cursor that supports chaining
        mock_cursor = MagicMock()
        mock_cursor.sort.return_value = []
        mock_cursor.__iter__.return_value = iter([])
        
        mock_db.fitness_classes.find.return_value = mock_cursor
        mock_db.fitness_classes.find_one.return_value = None
        mock_db.users.find_one.return_value = None
        mock_db.bookings.find.return_value = mock_cursor
        yield mock_db


@pytest.fixture
def client():
    """FastAPI test client"""
    return TestClient(app)


@pytest.fixture
def mock_db():
    """Mock database"""
    return MagicMock()


@pytest.fixture
def test_user():
    """Test user data"""
    return {
        "_id": "507f1f77bcf86cd799439011",
        "name": "Test User",
        "email": "test@example.com",
        "hashed_password": "$2b$12$1234567890abcdefghijklmnopqrst",
        "created_at": datetime.utcnow(),
    }


@pytest.fixture
def test_token(test_user):
    """Generate test JWT token"""
    token, _ = create_access_token(
        user_id=test_user["_id"],
        email=test_user["email"]
    )
    return token


@pytest.fixture
def auth_headers(test_token):
    """Authorization headers for test requests"""
    return {"Authorization": f"Bearer {test_token}"}


@pytest.fixture
def test_class():
    """Test fitness class data"""
    return {
        "_id": "507f1f77bcf86cd799439012",
        "name": "Yoga Flow",
        "date_time": datetime.utcnow() + timedelta(days=1),
        "instructor": "John Doe",
        "available_slots": 20,
        "booked_slots": 0,
        "created_by": "507f1f77bcf86cd799439011",
        "created_at": datetime.utcnow(),
    }


@pytest.fixture
def test_booking(test_user, test_class):
    """Test booking data"""
    return {
        "_id": "507f1f77bcf86cd799439013",
        "class_id": test_class["_id"],
        "user_id": test_user["_id"],
        "client_name": "Alice Johnson",
        "client_email": "alice@example.com",
        "created_at": datetime.utcnow(),
    }
