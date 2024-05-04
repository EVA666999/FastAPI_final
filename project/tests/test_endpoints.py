from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_for_post_user():
    response = client.post("/auth/register/", json={"username": "admin", "password": "123456"})
    assert response.status_code == 200
    assert response.json() == {"username": "admin", "password": "123456"}

def test_for_login_user():
    response = client.post("/auth/login/", json={"username": "admin", "password": "123456"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    access_token = response.json()["access_token"]
    response = client.get("/protected_resource", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200


def test_for_get_user():
    response = client.post("/auth/login/", json={"username": "admin", "password": "123456"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    access_token = response.json()["access_token"]
    response = client.get("/users/admin", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert response.json() == {"username": "admin", "password": "123456"}

def test_for_currency():
    response = client.post("/auth/login/", json={"username": "admin", "password": "123456"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    access_token = response.json()["access_token"]
    response = client.post("/currency/exchange", json={"source": "EUR", "currency": "USD"}, headers={"Authorization": f"Bearer {access_token}"})
    
    assert response.status_code == 200
    assert bool(response.json()["success"]) is True

def test_for_list():
    response = client.get("/currency/list/")
    assert response.status_code == 200
    assert bool(response.json()["success"]) is True