# LibraryProject Setup

## Django Development Environment Setup

### 1. Install Django

1. **Ensure Python is Installed:**
   - Verify Python installation: `python --version`

2. **Install Django:**
   - Command: `pip install django`

### 2. Create Your Django Project

1. **Create a New Django Project:**
   - Command: `django-admin startproject LibraryProject`

### 3. Run the Development Server

1. **Navigate to Project Directory:**
   - Command: `cd 0x1.Introduction_to_Django/LibraryProject`

2. **Start the Development Server:**
   - Command: `python manage.py runserver`
   - Access URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 4. Explore the Project Structure

1. **`settings.py`:** Configuration for the Django project
2. **`urls.py`:** URL declarations for the project
3. **`manage.py`:** Command-line utility for project management

### 5. GitHub Repository Setup

1. **Initialize Git Repository (if not done already):**
   - Command: `git init`

2. **Add Remote Repository:**
   - Command: `git remote add origin https://github.com/yourusername/Alx_DjangoLearnLab.git`

3. **Create and Switch to Main Branch:**
   - Command: `git branch -M main`

4. **Add and Commit Files:**
   - Command: `git add .`
   - Command: `git commit -m "Initial commit: Set up Django project LibraryProject"`

5. **Push to GitHub:**
   - Command: `git push -u origin main`

6. **Verify Directory Structure on GitHub:**
   - Ensure the directory `0x1.Introduction_to_Django/LibraryProject/` is correctly set up.

# README.md

## Permissions and Groups Setup

### Custom Permissions
- `can_view`: Can view MyModel
- `can_create`: Can create MyModel
- `can_edit`: Can edit MyModel
- `can_delete`: Can delete MyModel

### Groups
- **Editors**: `can_edit`, `can_create`
- **Viewers**: `can_view`
- **Admins**: `can_view`, `can_create`, `can_edit`, `can_delete`

### Usage
- Use `@permission_required('myapp.can_edit', raise_exception=True)` to protect views.
- Assign users to groups via Django admin or programmatically.


# Security Measures

## Settings
- `DEBUG = False`: Disable debug mode in production.
- `SECURE_BROWSER_XSS_FILTER = True`: Enable XSS filter.
- `X_FRAME_OPTIONS = 'DENY'`: Prevent clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevent MIME type sniffing.
- `CSRF_COOKIE_SECURE = True`: Ensure CSRF cookies are sent over HTTPS.
- `SESSION_COOKIE_SECURE = True`: Ensure session cookies are sent over HTTPS.

## CSRF Protection
- Ensure all forms include `{% csrf_token %}`.

## SQL Injection Prevention
- Use Django ORM to parameterize queries.

## Content Security Policy (CSP)
- Use `django-csp` middleware to set CSP headers.

# settings.py
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# Use HSTS to tell browsers to only use HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Additional security headers
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
