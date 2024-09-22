# Social Media API

This Django-based API provides the foundation for a social media platform with user authentication.

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## User Authentication

### Register a new user

POST `/api/accounts/register/`

Request body:
```json
{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "securepassword123",
    "bio": "Optional bio"
}
```

### Login

POST `/api/accounts/login/`

Request body:
```json
{
    "username": "existinguser",
    "password": "userpassword"
}
```

Both endpoints return an authentication token upon successful operation.

## User Model

The custom User model extends Django's AbstractUser and includes additional fields:
- `bio`: Text field for user biography
- `profile_picture`: Image field for user's profile picture
- `followers`: Many-to-Many relationship with itself for following functionality

For more details, refer to the `accounts/models.py` file.