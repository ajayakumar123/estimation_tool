import pytest
from app import app, mongo
import json
import pdb

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_registration(client):
    response = client.post('/register', data=dict(
        user_name='ajay',
        email='ajay@gmail.com',
        password='ajay@123',
        confirm_password='ajay@123'
    ), follow_redirects=True)
    #pdb.set_trace()
    assert response.status_code == 200

def test_login(client):
    response = client.post('/login', data=dict(
        email='ajay@example.com',
        password='ajay@123'
    ), follow_redirects=True)
    assert response.status_code == 200

def test_estimation(client):
    response = client.post('/estimation', data=dict(
        task_details='Test Task3',
        task_complexity='High',
        task_size='Large',
        task_type='Development',
        additional_notes='Some additional notes',
        estimated_effort=10
    ), follow_redirects=True)
    assert response.status_code == 200

def test_get_estimate(client):
    input_data = {
        "task_complexity": "high",
        "task_size": "large",
        "task_type": "development"
    }

    
    response = client.post('/api/get_estimate', json=input_data)
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data['success'] == True

def test_logout(client):
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
