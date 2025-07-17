from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.dog import Dog
from schemas.dog_schema import DogCreate, DogRead
from database import get_session
from models.training_session import TrainingSession
from schemas.training_session_schema import TrainingSessionRead


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


@router.get("/{dog_id}/training_sessions", response_model=list[TrainingSessionRead])
def get_training_sessions_for_dog(dog_id: int, session: Session = Depends(get_session)):
    dog = session.get(Dog, dog_id)
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    training_sessions = session.exec(select(TrainingSession).where(TrainingSession.dog_id == dog_id)).all()
    return training_sessions
