# integration tests for authentication endpoints
import pytest

from app import create_app
from app.core.extensions import db


@pytest.fixture()
def client(tmp_path, monkeypatch):
    database_path = tmp_path / "test.db"
    monkeypatch.setenv("FLASK_ENV", "testing")
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{database_path}")

    app = create_app()
    app.config.update(TESTING=True)

    with app.app_context():
        db.drop_all()
        db.create_all()

    with app.test_client() as test_client:
        yield test_client

    with app.app_context():
        db.session.remove()
        db.drop_all()


def test_register_creates_user(client):
    response = client.post(
        "/auth/register",
        json={"email": "user@example.com", "password": "secret123"},
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == "User registered"


def test_duplicate_registration_returns_conflict(client):
    client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "secret123"},
    )

    response = client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "secret123"},
    )

    assert response.status_code == 409
    assert "already exists" in response.get_json()["error"].lower()


def test_login_returns_token_for_valid_credentials(client):
    client.post(
        "/auth/register",
        json={"email": "login@example.com", "password": "secret123"},
    )

    response = client.post(
        "/auth/login",
        json={"email": "login@example.com", "password": "secret123"},
    )

    assert response.status_code == 200
    assert "access_token" in response.get_json()
