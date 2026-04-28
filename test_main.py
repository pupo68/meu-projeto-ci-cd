from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "message": "API CI/CD funcional"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_calculate_sum():
    response = client.get("/soma?a=10&b=20")
    assert response.status_code == 200
    assert response.json() == {"resultado": 30}

def test_read_item_premium():
    response = client.get("/items/150")
    assert response.status_code == 200
    assert response.json()["category"] == "premium"

def test_reverse_text():
    response = client.get("/reverse?texto=python")
    assert response.status_code == 200
    assert response.json()["invertido"] == "nohtyp"
