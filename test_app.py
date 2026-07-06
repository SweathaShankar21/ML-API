from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check_endpoint():
    """Validates that the API root starts up smoothly."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_endpoint_success():
    """Validates that valid payloads yield a successful code."""
    valid_payload = {"feature_1": 5.1, "feature_2": 3.5, "feature_3": 1.4, "feature_4": 0.2}
    response = client.post("/predict", json=valid_payload)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_endpoint_validation_error():
    """Validates that corrupt payload configurations are caught cleanly (422 Error)."""
    invalid_payload = {"feature_1": "not_a_number", "feature_2": 3.5}
    response = client.post("/predict", json=invalid_payload)
    assert response.status_code == 422
