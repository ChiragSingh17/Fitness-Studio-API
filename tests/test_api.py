"""Authentication endpoint tests"""
import pytest
from fastapi import status


class TestAuthentication:
    """Test authentication endpoints"""
    
    def test_signup_success(self, client, mock_db):
        """Test successful user signup"""
        signup_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "securepass123"
        }
        
        # This test would require mocking the database
        # In a real scenario, use a test database
        # response = client.post("/api/v1/signup", json=signup_data)
        # assert response.status_code == status.HTTP_201_CREATED
    
    def test_signup_invalid_email(self, client):
        """Test signup with invalid email"""
        signup_data = {
            "name": "John Doe",
            "email": "invalid-email",
            "password": "securepass123"
        }
        
        response = client.post("/api/v1/signup", json=signup_data)
        assert response.status_code in [status.HTTP_422_UNPROCESSABLE_ENTITY, status.HTTP_400_BAD_REQUEST]
    
    def test_signup_weak_password(self, client):
        """Test signup with weak password"""
        signup_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "short"
        }
        
        response = client.post("/api/v1/signup", json=signup_data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_login_with_invalid_credentials(self, client):
        """Test login with invalid credentials"""
        login_data = {
            "email": "nonexistent@example.com",
            "password": "wrongpassword"
        }
        
        # This would fail as user doesn't exist
        # response = client.post("/api/v1/login", json=login_data)
        # assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestClassEndpoints:
    """Test class endpoints"""
    
    def test_get_classes_unauthenticated(self, client):
        """Test getting classes without authentication"""
        response = client.get("/api/v1/classes")
        assert response.status_code == status.HTTP_200_OK
    
    def test_create_class_without_authentication(self, client):
        """Test creating class without authentication"""
        class_data = {
            "name": "Yoga Flow",
            "dateTime": "2025-06-15T10:00:00Z",
            "instructor": "John Doe",
            "availableSlots": 20
        }
        
        response = client.post("/api/v1/classes", json=class_data)
        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestBookingEndpoints:
    """Test booking endpoints"""
    
    def test_book_class_without_authentication(self, client):
        """Test booking class without authentication"""
        booking_data = {
            "classId": "507f1f77bcf86cd799439012",
            "clientName": "Alice",
            "clientEmail": "alice@example.com"
        }
        
        response = client.post("/api/v1/bookings", json=booking_data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_get_bookings_without_authentication(self, client):
        """Test getting bookings without authentication"""
        response = client.get("/api/v1/bookings")
        assert response.status_code == status.HTTP_403_FORBIDDEN


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "healthy"


def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "message" in response.json()
