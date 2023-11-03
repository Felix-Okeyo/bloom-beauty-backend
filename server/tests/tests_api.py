from app import app
from app import create_app
import json

app = create_app() 

# Initialize the test client
client = app.test_client()

def test_home_endpoint():
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "Welcome to the Bloom Beauty Management System API" in data["message"]

def test_register_and_login():
    # Register a new user
    registration_data = {
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "ph_address": "123 Main St",
        "password": "password123",
        "telephone": 1234567890,
        "city_town": "Sample City"
    }

    response = client.post('/register', data=json.dumps(registration_data), content_type='application/json')
    assert response.status_code == 201

    # Login with the registered user
    login_data = {
        "username": "johndoe",
        "password": "password123"
    }

    response = client.post('/login', data=json.dumps(login_data), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "access_token" in data

def test_invalid_login():
    # Attempt to login with incorrect credentials
    invalid_login_data = {
        "username": "johndoe",
        "password": "wrong_password"
    }

    response = client.post('/login', data=json.dumps(invalid_login_data), content_type='application/json')
    assert response.status_code == 401
