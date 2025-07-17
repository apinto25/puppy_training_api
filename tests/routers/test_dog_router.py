from datetime import date
from fastapi.testclient import TestClient
from sqlmodel import Session
from models.dog import Dog


def test_get_dogs(session: Session, client: TestClient):

    dog_1 = Dog(name="Tony", breed="Mestizo", birth_date=date(2020, 1, 1))
    session.add(dog_1)
    session.commit()

    response = client.get("/dogs/")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["name"] == "Tony"


def test_get_dog_by_id(session: Session, client: TestClient):
    dog_1 = Dog(name="Max", breed="Labrador", birth_date=date(2019, 5, 20))
    session.add(dog_1)
    session.commit()
    session.refresh(dog_1)

    response = client.get(f"/dogs/{dog_1.id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == dog_1.id
    assert data["name"] == "Max"


def test_get_dog_by_id_not_found(client: TestClient):
    response = client.get("/dogs/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Dog not found"


def test_create_dog(client: TestClient):
    payload = {
        "name": "Bella",
        "breed": "Beagle",
        "birth_date": "2021-07-10"
    }
    response = client.post("/dogs/", json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Bella"
    assert data["breed"] == "Beagle"
    assert data["birth_date"] == "2021-07-10"


def test_delete_dog(session: Session, client: TestClient):
    dog_1 = Dog(name="Rocky", breed="Boxer", birth_date=date(2018, 3, 15))
    session.add(dog_1)
    session.commit()
    session.refresh(dog_1)

    response = client.delete(f"/dogs/{dog_1.id}")
    assert response.status_code == 204

    # Confirm deletion
    response = client.get(f"/dogs/{dog_1.id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Dog not found"
