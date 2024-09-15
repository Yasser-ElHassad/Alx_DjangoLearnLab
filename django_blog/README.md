# Django Blog Authentication System

This document outlines the authentication system implemented in the Django Blog project.

## Features

1. User Registration
2. User Login
3. User Logout
4. Profile Management

## Setup Instructions

1. Ensure all required packages are installed: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Start the development server: `python manage.py runserver`

## Usage Guide

### Registration

- Navigate to `/register/`
- Fill out the registration form with username, email, and password
- Upon successful registration, you'll be logged in and redirected to the home page

### Login

- Navigate to `/login/`
- Enter your username and password
- Upon successful login, you'll be redirected to the home page

### Logout

- Click on the logout link or navigate to `/logout/`
- You'll be logged out and redirected to the home page

### Profile Management

- Navigate to `/profile/`
- Update your profile information (username, email, first name, last name)
- Submit the form to save changes

## Testing

To test each feature:

1. Registration: Try registering with valid and invalid data
2. Login: Attempt to log in with correct and incorrect credentials
3. Logout: Ensure you're redirected and can't access protected pages after logout
4. Profile: Update profile information and verify changes are saved

## Security Notes

- CSRF protection is enabled for all forms
- Passwords are securely hashed using Django's built-in hashing algorithms
- Access to the profile page is restricted to authenticated users only