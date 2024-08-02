# Django Token Authentication Example

This project demonstrates how to implement token-based authentication in a Django REST Framework application. Token authentication is a simple and secure way to handle authentication for your API endpoints.

## Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Django REST Framework authtoken

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/alby-tomy/django-rest-framework--DRF--authentication.git
cd django-rest-framework--DRF--authentication

```
### 2.Create Virtual Environment and Activate it
```bash
python -m venv venv
source venv/bin/activate
```

### 3.Install the Required Packages
```bash
pip install django djangorestframework
```

## Models and Serializers
- #### Model
  - Importing User model by `from django.contrib.auth.models import User`
  - add `'rest_framework.authtoken'` in DRF_authentication/settings.py to use Token table for token authentication and import it by `from rest_framework.authtoken.models import Token`

- ### Serializer
  - Defines the `RegisterSerializer` and `LoginSerializer` with custom validation for registration.

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

### API Endpoints
  - #### 1. Register a New User
    Endpoint : `register/`
    Method : `POST `
    
  - #### 2. Login
    Endpoint : `login/`
    Method : `POST`
    
  - #### 3. Get All Users
    Endpoint : `userlist`
    Method : `GET `

### Testing the API
You can use tools like Postman or Curl to test the endpoints. Here are some example requests:
#### Register a User
```bash
  curl -X POST http://127.0.0.1:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword"}'
```

#### Login
```bash
  curl -X POST http://127.0.0.1:8000/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword"}'
```

### Get Users List
```bash
  curl -X GET http://127.0.0.1:8000/userlist/ \
  -H "Content-Type: application/json"
```

## This should cover the basic setup and usage of token authentication in a Django REST Framework application.
