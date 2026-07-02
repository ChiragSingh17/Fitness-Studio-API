# Fitness Studio Booking API - Development Guide

This file documents the project structure, conventions, and development practices for the Fitness Studio Booking API.

## Project Overview

A FastAPI-based REST API for managing fitness class bookings with JWT authentication and MongoDB database.

## Technology Stack

- **Framework**: FastAPI 0.104.1
- **Database**: MongoDB 4.6.0
- **Authentication**: JWT (python-jose)
- **Password Hashing**: Bcrypt
- **Validation**: Pydantic 2.5.0
- **Testing**: Pytest 7.4.3

## Development Setup

1. Create virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Unix)
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file from `.env.example`
5. Run: `python -m uvicorn main:app --reload`

## Project Structure

```
app/
├── models/          # Database models
├── schemas/         # Pydantic schemas for validation
├── routes/          # API route handlers
├── utils/           # Utility functions (auth, timezone, etc.)
├── config.py        # Configuration
└── database.py      # Database connection

tests/               # Test files
main.py              # FastAPI application entry point
seeds.py             # Database seeding script
examples.py          # API usage examples
```

## Code Conventions

- Use type hints for all functions
- Document public functions with docstrings
- Follow PEP 8 style guide
- Use meaningful variable names
- Keep functions small and focused

## API Endpoints

All endpoints follow the pattern: `/api/v1/{resource}`

### Authentication
- `POST /signup` - Register new user
- `POST /login` - Authenticate and get token

### Classes
- `GET /classes` - Get all upcoming classes
- `POST /classes` - Create a new class (auth required)

### Bookings
- `POST /bookings` - Book a class (auth required)
- `GET /bookings` - Get user's bookings (auth required)

## Testing

Run tests with: `pytest`

For coverage: `pytest --cov=app tests/`

## Deployment

Use Docker and Docker Compose:

```bash
docker-compose up
```

## Environment Variables

All configuration is in `.env` file:
- MONGODB_URL: MongoDB connection string
- DATABASE_NAME: Database name
- JWT_SECRET_KEY: Secret key for JWT
- JWT_ALGORITHM: Algorithm for JWT (default: HS256)
- TOKEN_EXPIRE_MINUTES: Token expiration time
- TIMEZONE: Timezone for class times (default: Asia/Kolkata)

## Common Tasks

### Add a new endpoint
1. Create schema in `app/schemas/`
2. Create route in `app/routes/`
3. Include router in `main.py`
4. Add tests in `tests/`

### Add a new model
1. Create model file in `app/models/`
2. Create corresponding schema in `app/schemas/`
3. Create indexes if needed in MongoDB

### Database Seeding
Run `python seeds.py` to populate test data.

## Git Workflow

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -m "Add feature"`
3. Push: `git push origin feature/your-feature`
4. Open Pull Request

## Troubleshooting

### MongoDB Connection Issues
- Ensure MongoDB is running
- Check connection string in `.env`

### Import Errors
- Activate virtual environment
- Install dependencies: `pip install -r requirements.txt`

### Port Already in Use
- Change port: `python -m uvicorn main:app --port 8001`

## Additional Resources

- FastAPI Docs: https://fastapi.tiangolo.com/
- MongoDB Docs: https://docs.mongodb.com/
- PyJWT: https://pyjwt.readthedocs.io/
- Pydantic: https://docs.pydantic.dev/

---
Last Updated: 2025-01-15
