import pytest
from datetime import date
from fastapi.testclient import TestClient
from sqlmodel import Session
from models.command import Command


def test_get_commands(session: Session, client: TestClient):
    command_1 = Command(name="Sit", description="Dog sits down")
    session.add(command_1)
    session.commit()
    response = client.get("/commands/")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["name"] == "Sit"


def test_get_command_by_id(session: Session, client: TestClient):
    command_1 = Command(name="Stay", description="Dog stays")
    session.add(command_1)
    session.commit()
    session.refresh(command_1)
    response = client.get(f"/commands/{command_1.id}")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == command_1.id
    assert data["name"] == "Stay"


def test_get_command_by_id_not_found(client: TestClient):
    response = client.get("/commands/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Command not found"


def test_create_command(client: TestClient):
    payload = {
        "name": "Down",
        "description": "Dog lies down"
    }
    response = client.post("/commands/", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "Down"
    assert data["description"] == "Dog lies down"


def test_delete_command(session: Session, client: TestClient):
    command_1 = Command(name="Come", description="Dog comes here")
    session.add(command_1)
    session.commit()
    session.refresh(command_1)
    response = client.delete(f"/commands/{command_1.id}")
    assert response.status_code == 204
    # Confirm deletion
    response = client.get(f"/commands/{command_1.id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Command not found"
