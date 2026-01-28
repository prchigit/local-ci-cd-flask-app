from app.main import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Production Flask App" in response.json["message"]


def test_add():
    client = app.test_client()
    response = client.get("/add?a=5&b=10")
    assert response.status_code == 200
    assert response.json["result"] == 15


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

