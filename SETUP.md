# 🎉 Fitness Studio Booking API - Project Complete!

## 📦 Project Summary

A fully functional **Fitness Studio Booking API** has been created with:

✅ **FastAPI** - Modern, fast web framework
✅ **MongoDB** - NoSQL database for flexibility
✅ **JWT Authentication** - Secure token-based auth
✅ **Complete CRUD Operations** - For users, classes, and bookings
✅ **Input Validation** - Pydantic schemas for all endpoints
✅ **Error Handling** - Comprehensive error responses
✅ **Timezone Support** - All times in IST (India Standard Time)
✅ **Unit Tests** - pytest test suite
✅ **Auto Documentation** - Swagger UI & ReDoc
✅ **Seed Data** - Sample users, classes, and bookings

---

## 🚀 Quick Start (5 minutes)

### 1. Setup Environment
```bash
cd "Fitness Studio"
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Mac/Linux
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure .env
```bash
cp .env.example .env
```

### 4. Start MongoDB
```bash
# Option 1: Local MongoDB
mongod

# Option 2: MongoDB Atlas (Cloud)
# Update MONGODB_URL in .env with your connection string
```

### 5. Seed Database
```bash
python seeds.py
```

### 6. Run API
```bash
python -m uvicorn main:app --reload
```

**API is now running at:** `http://localhost:8000`

---

## 📚 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/v1/signup` | ❌ | Register new user |
| POST | `/api/v1/login` | ❌ | Login & get token |
| GET | `/api/v1/classes` | ❌ | View all classes |
| POST | `/api/v1/classes` | ✅ | Create new class |
| POST | `/api/v1/bookings` | ✅ | Book a class |
| GET | `/api/v1/bookings` | ✅ | View user bookings |

---

## 💻 API Usage Examples

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

### Book a Class (with token from login)
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

---

## 📁 Project Structure

```
Fitness Studio/
│
├── app/                          # Main application package
│   ├── __init__.py
│   ├── config.py                # Settings and configuration
│   ├── database.py              # MongoDB connection
│   │
│   ├── models/                  # Database models
│   │   ├── __init__.py
│   │   ├── user.py              # User model
│   │   ├── fitness_class.py      # FitnessClass model
│   │   └── booking.py            # Booking model
│   │
│   ├── schemas/                 # Pydantic validation schemas
│   │   ├── __init__.py
│   │   ├── user.py              # User schemas (SignUp, Login, Response)
│   │   ├── fitness_class.py      # Class schemas (Create, Response)
│   │   └── booking.py            # Booking schemas (Create, Response)
│   │
│   ├── routes/                  # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py              # /signup, /login endpoints
│   │   ├── classes.py            # /classes endpoints
│   │   └── booking.py            # /bookings endpoints
│   │
│   └── utils/                   # Utility functions
│       ├── __init__.py
│       ├── auth.py              # JWT & password hashing
│       ├── timezone.py          # Timezone conversions
│       └── dependencies.py      # FastAPI dependencies
│
├── tests/                       # Unit tests
│   ├── conftest.py              # Pytest configuration & fixtures
│   └── test_api.py              # API endpoint tests
│
├── main.py                      # FastAPI application entry point
├── seeds.py                     # Database seeding script
├── examples.py                  # Usage examples
│
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore file
├── pytest.ini                  # Pytest configuration
├── Dockerfile                  # Docker image definition
├── docker-compose.yml          # Docker Compose configuration
│
├── README.md                   # Full documentation
└── .github/
    └── copilot-instructions.md # Development guidelines
```

---

## 🔐 Security Features

✅ **Password Hashing** - Bcrypt with salt
✅ **JWT Tokens** - Secure token authentication
✅ **Token Expiration** - 30-minute expiration (configurable)
✅ **Input Validation** - Pydantic schemas
✅ **Email Validation** - EmailStr validation
✅ **CORS Support** - Cross-origin requests allowed
✅ **Error Handling** - No sensitive info in errors

---

## 🧪 Testing

Run tests:
```bash
pytest -v                    # Run with verbose output
pytest --cov=app tests/      # Run with coverage
pytest tests/test_api.py     # Run specific test file
```

---

## 🐳 Docker Deployment

Build and run with Docker:
```bash
# Build images
docker-compose build

# Run services
docker-compose up

# Run in background
docker-compose up -d

# Stop services
docker-compose down
```

Services:
- **API**: `http://localhost:8000`
- **MongoDB**: `mongodb://localhost:27017`

---

## 📖 Documentation

Access interactive documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

---

## 🔍 Key Features Explained

### 1. Authentication
- Users sign up with name, email, password
- Passwords hashed with bcrypt
- Login returns JWT token valid for 30 minutes
- Token required for protected endpoints

### 2. Class Management
- Any authenticated user can create classes
- Classes include: name, date/time, instructor, available slots
- Only future classes are returned by GET /classes
- Classes stored with UTC timestamps

### 3. Booking System
- Users can book available slots
- Prevents duplicate bookings per user
- Prevents overbooking
- Automatic slot counting
- Users can view their booking history

### 4. Timezone Management
- All internal storage: UTC
- API display: IST (Asia/Kolkata)
- Configurable timezone via .env
- Automatic conversion with pytz

---

## ⚙️ Configuration

Edit `.env` to customize:

```env
# MongoDB connection
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=fitness_studio

# JWT security
JWT_SECRET_KEY=your-secret-key-change-in-production
JWT_ALGORITHM=HS256
TOKEN_EXPIRE_MINUTES=30

# Timezone
TIMEZONE=Asia/Kolkata
```

---

## 📊 Database Collections

### Users Collection
```javascript
{
  "_id": ObjectId,
  "name": string,
  "email": string (unique),
  "hashed_password": string,
  "created_at": datetime
}
```

### Fitness Classes Collection
```javascript
{
  "_id": ObjectId,
  "name": string,
  "date_time": datetime,
  "instructor": string,
  "available_slots": number,
  "booked_slots": number,
  "created_by": string (user_id),
  "created_at": datetime
}
```

### Bookings Collection
```javascript
{
  "_id": ObjectId,
  "class_id": ObjectId,
  "user_id": ObjectId,
  "client_name": string,
  "client_email": string,
  "created_at": datetime
}
```

---

## 🚨 Error Handling

All errors return standard JSON format:
```json
{
  "detail": "Error message",
  "status_code": 400
}
```

Common error codes:
- **400** - Bad Request (validation error, duplicate user, etc.)
- **401** - Unauthorized (invalid token)
- **403** - Forbidden (missing authentication)
- **404** - Not Found (resource doesn't exist)
- **422** - Unprocessable Entity (validation failed)
- **500** - Server Error

---

## 📝 Postman Integration

Import API into Postman:
1. Open Postman
2. Click "Import" → "Link"
3. Paste: `http://localhost:8000/openapi.json`

Or manually create requests using the endpoint examples.

---

## 🐛 Troubleshooting

### MongoDB Connection Error
```
Error: Failed to connect to MongoDB
```
**Solution**: Check MONGODB_URL in .env, ensure mongod is running

### JWT Token Invalid
```
Error: Could not validate credentials
```
**Solution**: Token may be expired. Login again to get a new token

### Port 8000 Already in Use
```
Error: Address already in use
```
**Solution**: Change port: `python -m uvicorn main:app --port 8001`

### Import Errors
```
Error: ModuleNotFoundError
```
**Solution**: Activate venv and install dependencies: `pip install -r requirements.txt`

---

## 📈 Future Enhancements

Consider adding:
- Pagination for list endpoints
- Redis caching for frequently accessed data
- Rate limiting
- Email verification on signup
- Class reviews/ratings
- Instructor profiles
- Payment integration
- Notification system
- Admin dashboard

---

## 📄 License

This project is open source under MIT License.

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add feature"`
4. Push: `git push origin feature/your-feature`
5. Open Pull Request

---

## 📞 Support

For issues or questions:
1. Check README.md for detailed documentation
2. Check `.github/copilot-instructions.md` for development guidelines
3. Open an issue on GitHub

---

## ✨ What's Included

✅ Full API implementation
✅ JWT authentication system
✅ MongoDB integration
✅ Comprehensive error handling
✅ Input validation (Pydantic)
✅ Unit tests with pytest
✅ Database seeding script
✅ API usage examples
✅ Docker & Docker Compose setup
✅ Detailed README with cURL examples
✅ Development guidelines
✅ Auto-generated API documentation

---

## 🎯 Next Steps

1. ✅ Clone repository
2. ✅ Create virtual environment
3. ✅ Install dependencies
4. ✅ Setup `.env` file
5. ✅ Start MongoDB
6. ✅ Run `python seeds.py`
7. ✅ Run `python -m uvicorn main:app --reload`
8. ✅ Visit `http://localhost:8000/docs` for interactive API docs
9. ✅ Test endpoints with provided curl examples
10. ✅ Deploy to production!

---

**Built with ❤️ using FastAPI and MongoDB**

Last Updated: 2025-01-15
