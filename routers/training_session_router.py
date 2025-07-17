from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models.training_session import TrainingSession
from schemas.training_session_schema import TrainingSessionRead, TrainingSessionWrite

router = APIRouter(prefix="/training_sessions", tags=["training_sessions"])


@router.get("/{session_id}", response_model=TrainingSessionRead)
def get_training_session(session_id: int, session: Session = Depends(get_session)):
    training_session = session.get(TrainingSession, session_id)
    if not training_session:
        raise HTTPException(status_code=404, detail="Training session not found")
    return training_session


@router.post("/", status_code=201, response_model=TrainingSessionRead)
def create_training_session(training_session: TrainingSessionWrite, session: Session = Depends(get_session)):
    db_training_session = TrainingSession.model_validate(training_session)
    session.add(db_training_session)
    session.commit()
    session.refresh(db_training_session)
    return db_training_session


@router.delete("/{session_id}", status_code=204)
def delete_training_session(session_id: int, session: Session = Depends(get_session)):
    training_session = session.get(TrainingSession, session_id)
    if not training_session:
        raise HTTPException(status_code=404, detail="Training session not found")
    session.delete(training_session)
    session.commit()
