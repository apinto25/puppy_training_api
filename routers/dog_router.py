from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.dog import Dog
from schemas.dog_schema import DogCreate, DogRead
from database import get_session


router = APIRouter(prefix="/dogs", tags=["dogs"])


@router.get("/", response_model=list[DogRead])
def get_dogs(session: Session = Depends(get_session)):
    dogs = session.exec(select(Dog)).all()
    return dogs


@router.get("/{dog_id}", response_model=DogRead)
def get_dog_by_id(dog_id: int, session: Session = Depends(get_session)):
    dog = session.get(Dog, dog_id)
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    return dog


@router.post("/", status_code=201, response_model=DogRead)
def create_dog(dog: DogCreate, session: Session = Depends(get_session)):
    db_dog = Dog.model_validate(dog)
    session.add(db_dog)
    session.commit()
    session.refresh(db_dog)
    return db_dog


@router.delete("/{dog_id}", status_code=204)
def delete_dog(dog_id: int, session: Session = Depends(get_session)):
    dog = session.get(Dog, dog_id)
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    session.delete(dog)
    session.commit()
    return None
