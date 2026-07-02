"""
API Usage Examples

This file demonstrates how to use the Fitness Studio Booking API
with examples in both Python requests and cURL format.
"""

# ============================================================================
# PYTHON EXAMPLES
# ============================================================================

import requests
import json
from typing import Optional

# API Base URL
BASE_URL = "http://localhost:8000/api/v1"


class FitnessStudioAPI:
    """Client for Fitness Studio API"""
    
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.token: Optional[str] = None
        self.user_id: Optional[str] = None
    
    def signup(self, name: str, email: str, password: str) -> dict:
        """Sign up a new user"""
        response = requests.post(
            f"{self.base_url}/signup",
            json={
                "name": name,
                "email": email,
                "password": password
            }
        )
        response.raise_for_status()
        return response.json()
    
    def login(self, email: str, password: str) -> dict:
        """Login and get access token"""
        response = requests.post(
            f"{self.base_url}/login",
            json={
                "email": email,
                "password": password
            }
        )
        response.raise_for_status()
        data = response.json()
        self.token = data["access_token"]
        return data
    
    def get_headers(self) -> dict:
        """Get authorization headers"""
        if not self.token:
            raise ValueError("Not authenticated. Call login() first.")
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def get_classes(self) -> list:
        """Get all upcoming classes"""
        response = requests.get(f"{self.base_url}/classes")
        response.raise_for_status()
        return response.json()
    
    def create_class(
        self,
        name: str,
        date_time: str,
        instructor: str,
        available_slots: int
    ) -> dict:
        """Create a new fitness class"""
        response = requests.post(
            f"{self.base_url}/classes",
            headers=self.get_headers(),
            json={
                "name": name,
                "dateTime": date_time,
                "instructor": instructor,
                "availableSlots": available_slots
            }
        )
        response.raise_for_status()
        return response.json()
    
    def book_class(
        self,
        class_id: str,
        client_name: str,
        client_email: str
    ) -> dict:
        """Book a class"""
        response = requests.post(
            f"{self.base_url}/bookings",
            headers=self.get_headers(),
            json={
                "classId": class_id,
                "clientName": client_name,
                "clientEmail": client_email
            }
        )
        response.raise_for_status()
        return response.json()
    
    def get_bookings(self) -> list:
        """Get user's bookings"""
        response = requests.get(
            f"{self.base_url}/bookings",
            headers=self.get_headers()
        )
        response.raise_for_status()
        return response.json()


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

def python_example():
    """Example usage of the API client"""
    
    client = FitnessStudioAPI()
    
    # 1. Sign up
    print("1. Signing up...")
    user = client.signup(
        name="John Doe",
        email="john@example.com",
        password="securepass123"
    )
    print(f"✓ User created: {user}")
    
    # 2. Login
    print("\n2. Logging in...")
    token_data = client.login(
        email="john@example.com",
        password="securepass123"
    )
    print(f"✓ Logged in. Token: {token_data['access_token'][:20]}...")
    
    # 3. Get classes
    print("\n3. Getting classes...")
    classes = client.get_classes()
    print(f"✓ Found {len(classes)} classes")
    for cls in classes:
        print(f"  - {cls['name']} by {cls['instructor']}")
    
    # 4. Create a class
    print("\n4. Creating a new class...")
    new_class = client.create_class(
        name="Advanced Yoga",
        date_time="2025-06-20T10:00:00Z",
        instructor="John Doe",
        available_slots=15
    )
    print(f"✓ Class created: {new_class}")
    
    # 5. Book a class
    if classes:
        print(f"\n5. Booking a class...")
        booking = client.book_class(
            class_id=classes[0]["_id"],
            client_name="John Doe",
            client_email="john@example.com"
        )
        print(f"✓ Booking confirmed: {booking}")
    
    # 6. Get bookings
    print("\n6. Getting user bookings...")
    bookings = client.get_bookings()
    print(f"✓ User has {len(bookings)} bookings")
    for booking in bookings:
        print(f"  - Booked class: {booking['classId']}")


# ============================================================================
# CURL EXAMPLES
# ============================================================================

CURL_EXAMPLES = """
# 1. SIGN UP
curl -X POST "http://localhost:8000/api/v1/signup" \\
  -H "Content-Type: application/json" \\
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepass123"
  }'

# 2. LOGIN
curl -X POST "http://localhost:8000/api/v1/login" \\
  -H "Content-Type: application/json" \\
  -d '{
    "email": "john@example.com",
    "password": "securepass123"
  }'

# Response will be: {"access_token": "...", "token_type": "bearer", "expires_in": 1800}
# Save the access_token for use in authenticated requests

# 3. GET ALL CLASSES
curl -X GET "http://localhost:8000/api/v1/classes"

# 4. CREATE A CLASS (Requires authentication)
# Replace TOKEN with your access_token from login response
curl -X POST "http://localhost:8000/api/v1/classes" \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer TOKEN" \\
  -d '{
    "name": "HIIT Session",
    "dateTime": "2025-06-18T08:00:00Z",
    "instructor": "Jane Smith",
    "availableSlots": 15
  }'

# 5. BOOK A CLASS (Requires authentication)
# Replace CLASS_ID with actual class ID and TOKEN with your access_token
curl -X POST "http://localhost:8000/api/v1/bookings" \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer TOKEN" \\
  -d '{
    "classId": "CLASS_ID",
    "clientName": "Alice Johnson",
    "clientEmail": "alice@example.com"
  }'

# 6. GET USER BOOKINGS (Requires authentication)
# Replace TOKEN with your access_token
curl -X GET "http://localhost:8000/api/v1/bookings" \\
  -H "Authorization: Bearer TOKEN"

# 7. HEALTH CHECK
curl -X GET "http://localhost:8000/health"
"""


if __name__ == "__main__":
    print("=== Fitness Studio API - Usage Examples ===\n")
    
    print("To run Python examples, uncomment the line below:\n")
    print("# python_example()\n")
    
    print("=== cURL Examples ===\n")
    print(CURL_EXAMPLES)
    print("\n=== Tips ===")
    print("1. Replace 'TOKEN' with your actual access token from login response")
    print("2. Replace 'CLASS_ID' with an actual class ID from get classes response")
    print("3. Update email/password as needed")
    print("4. Ensure MongoDB is running at mongodb://localhost:27017")
    print("5. Ensure FastAPI server is running on http://localhost:8000")
