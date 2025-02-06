import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    response = client.get('/tasks')
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Data: {response.data}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code} with body {response.data}"
