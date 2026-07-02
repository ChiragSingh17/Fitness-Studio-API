# 💪 Fitness Studio Booking API

A modern REST API for managing fitness class bookings at a fictional fitness studio. Built with **FastAPI**, **MongoDB**, and **JWT Authentication**.

## ✨ Features

- 🔐 **JWT Authentication** - Secure user authentication with token-based access control
- 📚 **Fitness Classes** - Create, view, and manage fitness classes
- 🎫 **Class Booking** - Book available slots in fitness classes with overbooking prevention
- 👥 **User Management** - Sign up, login, and manage user profiles
- 🗓️ **Timezone Support** - All times stored in IST (Indian Standard Time)
- 📖 **Auto-generated Docs** - Interactive Swagger UI and ReDoc documentation
- 🧪 **Unit Tests** - Comprehensive test coverage
- 📝 **Request Validation** - Input validation using Pydantic
- 🛡️ **Error Handling** - Comprehensive error handling and logging

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | FastAPI 0.104.1 |
| **Database** | MongoDB 4.6.0 |
| **Authentication** | JWT (python-jose) |
| **Password Hashing** | Bcrypt |
| **Data Validation** | Pydantic 2.5.0 |
| **Web Server** | Uvicorn 0.24.0 |
| **Testing** | Pytest 7.4.3 |
| **Timezone Handling** | pytz 2023.3 |

## 📋 Prerequisites

- Python 3.8 or higher
- MongoDB 4.0 or higher (local or cloud)
- pip (Python package manager)
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd "Fitness Studio"
```

### 2. Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=fitness_studio
JWT_SECRET_KEY=your-super-secret-key-change-this-in-production
JWT_ALGORITHM=HS256
TOKEN_EXPIRE_MINUTES=30
TIMEZONE=Asia/Kolkata
```

### 5. Ensure MongoDB is Running

**Using MongoDB locally:**
```bash
mongod
```

**Or use MongoDB Atlas (Cloud):**
- Update `MONGODB_URL` in `.env` with your connection string

### 6. Seed the Database (Optional)

```bash
python seeds.py
```

This will populate the database with sample users, classes, and bookings.

### 7. Run the Application

```bash
python -m uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

## 📚 API Documentation

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔌 API Endpoints

### Authentication Endpoints

#### Sign Up
```http
POST /api/v1/signup
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepass123"
}
```

**Response** (201 Created):
```json
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00"
}
```

#### Login
```http
POST /api/v1/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepass123"
}
```

**Response** (200 OK):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

### Fitness Classes Endpoints

#### Get All Upcoming Classes
```http
GET /api/v1/classes
```

**Response** (200 OK):
```json
[
  {
    "_id": "507f1f77bcf86cd799439012",
    "name": "Yoga Flow",
    "dateTime": "2025-06-15T10:00:00",
    "instructor": "John Doe",
    "availableSlots": 20,
    "bookedSlots": 5,
    "createdBy": "507f1f77bcf86cd799439011",
    "createdAt": "2025-01-10T08:00:00"
  }
]
```

#### Create a New Class
```http
POST /api/v1/classes
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN

{
  "name": "Yoga Flow",
  "dateTime": "2025-06-15T10:00:00Z",
  "instructor": "John Doe",
  "availableSlots": 20
}
```

**Response** (201 Created):
```json
{
  "_id": "507f1f77bcf86cd799439012",
  "name": "Yoga Flow",
  "dateTime": "2025-06-15T10:00:00",
  "instructor": "John Doe",
  "availableSlots": 20,
  "bookedSlots": 0,
  "createdBy": "507f1f77bcf86cd799439011",
  "createdAt": "2025-01-15T10:30:00"
}
```

### Booking Endpoints

#### Book a Class
```http
POST /api/v1/bookings
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN

{
  "classId": "507f1f77bcf86cd799439012",
  "clientName": "Alice Johnson",
  "clientEmail": "alice@example.com"
}
```

**Response** (201 Created):
```json
{
  "_id": "507f1f77bcf86cd799439013",
  "classId": "507f1f77bcf86cd799439012",
  "clientName": "Alice Johnson",
  "clientEmail": "alice@example.com",
  "createdAt": "2025-01-15T11:00:00"
}
```

#### Get User Bookings
```http
GET /api/v1/bookings
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Response** (200 OK):
```json
[
  {
    "_id": "507f1f77bcf86cd799439013",
    "classId": "507f1f77bcf86cd799439012",
    "clientName": "Alice Johnson",
    "clientEmail": "alice@example.com",
    "createdAt": "2025-01-15T11:00:00"
  }
]
```

## 📝 cURL Examples

### Sign Up
```bash
curl -X POST "http://localhost:8000/api/v1/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepass123"
  }'
```

### Login
```bash
curl -X POST "http://localhost:8000/api/v1/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepass123"
  }'
```

### Get Classes
```bash
curl -X GET "http://localhost:8000/api/v1/classes"
```

### Create Class (Authenticated)
```bash
curl -X POST "http://localhost:8000/api/v1/classes" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "HIIT Session",
    "dateTime": "2025-06-18T08:00:00Z",
    "instructor": "Jane Smith",
    "availableSlots": 15
  }'
```

### Book a Class (Authenticated)
```bash
curl -X POST "http://localhost:8000/api/v1/bookings" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "classId": "507f1f77bcf86cd799439012",
    "clientName": "Alice Johnson",
    "clientEmail": "alice@example.com"
  }'
```

### Get User Bookings (Authenticated)
```bash
curl -X GET "http://localhost:8000/api/v1/bookings" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 📊 Postman Collection

You can import the API into Postman for easier testing:

1. Open Postman
2. Click **Import** → **Link**
3. Paste the Swagger URL: `http://localhost:8000/openapi.json`
4. Or manually create requests using the endpoint examples above

**Workflow:**
1. Sign up a new user
2. Login to get access token
3. Create a fitness class
4. View all classes
5. Book a class
6. View your bookings

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_api.py

# Run with coverage
pytest --cov=app tests/
```

## 📁 Project Structure

```
Fitness Studio/
├── app/
│   ├── __init__.py
│   ├── config.py              # Configuration settings
│   ├── database.py            # MongoDB connection
│   ├── models/
│   │   ├── user.py            # User model
│   │   ├── fitness_class.py    # FitnessClass model
│   │   └── booking.py          # Booking model
│   ├── schemas/
│   │   ├── user.py            # User Pydantic schemas
│   │   ├── fitness_class.py    # FitnessClass Pydantic schemas
│   │   └── booking.py          # Booking Pydantic schemas
│   ├── routes/
│   │   ├── auth.py            # Authentication routes
│   │   ├── classes.py          # Fitness class routes
│   │   └── booking.py          # Booking routes
│   └── utils/
│       ├── auth.py            # JWT & password utilities
│       ├── timezone.py        # Timezone utilities
│       └── dependencies.py    # FastAPI dependencies
├── tests/
│   ├── conftest.py            # Pytest configuration & fixtures
│   └── test_api.py            # API endpoint tests
├── main.py                    # FastAPI application entry point
├── seeds.py                   # Database seeding script
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## 🔐 Security Features

- **Password Hashing**: Bcrypt hashing with salt
- **JWT Tokens**: Secure token-based authentication
- **Token Expiration**: Tokens expire after 30 minutes (configurable)
- **Input Validation**: Pydantic models validate all inputs
- **CORS**: CORS middleware for cross-origin requests
- **Error Handling**: No sensitive information in error messages

## 🚨 Error Handling

The API returns proper HTTP status codes and error messages:

| Status Code | Meaning |
|------------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Unprocessable Entity |
| 500 | Internal Server Error |

**Error Response Example:**
```json
{
  "detail": "No available slots for this class",
  "status_code": 400
}
```

## 🎯 Key Features Implementation

### 1. Authentication
- JWT tokens with 30-minute expiration
- Password hashing with bcrypt
- Secure token verification

### 2. Overbooking Prevention
- Checks available slots before booking
- Prevents duplicate bookings per user
- Atomic slot updates

### 3. Timezone Management
- All times stored in IST (Asia/Kolkata)
- Automatic conversion from UTC
- Support for different timezones

### 4. Data Validation
- Email validation
- Password length requirements
- Request body validation
- Enum validation

## 🐛 Troubleshooting

### MongoDB Connection Error
```
Failed to connect to MongoDB
```
**Solution**: Ensure MongoDB is running and connection string is correct in `.env`

### JWT Token Invalid
```
Could not validate credentials
```
**Solution**: Make sure token is valid and not expired. Get a new token by logging in again.

### Port Already in Use
```
Address already in use
```
**Solution**: Change port in command: `python -m uvicorn main:app --port 8001`

### Import Errors
```
ModuleNotFoundError: No module named 'fastapi'
```
**Solution**: Ensure virtual environment is activated and dependencies are installed: `pip install -r requirements.txt`

## 📈 Performance Considerations

- **Database Indexes**: Consider adding indexes on frequently queried fields
- **Pagination**: Implement pagination for list endpoints in production
- **Caching**: Add Redis caching for frequently accessed classes
- **Rate Limiting**: Implement rate limiting for production use

## 🚀 Deployment

### Using Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables for Production

```env
MONGODB_URL=mongodb+srv://user:password@cluster.mongodb.net/fitness_studio
JWT_SECRET_KEY=use-a-strong-random-key-here
JWT_ALGORITHM=HS256
TOKEN_EXPIRE_MINUTES=30
TIMEZONE=Asia/Kolkata
```

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [JWT.io](https://jwt.io/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## 📝 License

This project is open source and available under the MIT License.

## 👥 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For issues or questions, please open an issue on GitHub.


**Built with ❤️ using FastAPI and MongoDB**
