from fastapi.testclient import TestClient
from src.main import app
from src.storage import save_expenses

client = TestClient(app)


def setup_function():
    save_expenses([])


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_expense():

    response = client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 100,
            "category": "Food",
            "date": "2026-08-01"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Expense added successfully"


def test_get_expenses():

    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 100,
            "category": "Food",
            "date": "2026-08-01"
        }
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_delete():

    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 100,
            "category": "Food",
            "date": "2026-08-01"
        }
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200