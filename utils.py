from datetime import date

from sqlmodel import Session, select, func

from models.training_session import TrainingSession


def get_dog_training_time(dog_id: int, day: date, session: Session) -> int:
    """
    Returns the total training duration (in minutes) for a given dog on a specific date.
    """
    result = session.exec(
        select(func.sum(TrainingSession.duration_minutes))
        .where(TrainingSession.dog_id == dog_id)
        .where(TrainingSession.date == day)
    ).one()
    return result or 0


def get_dog_training_sessions_by_date(dog_id: int, day: date, session: Session) -> list[TrainingSession]:
    """
    Returns a list of training sessions for a given dog on a specific date.
    """
    return session.exec(
        select(TrainingSession)
        .where(TrainingSession.dog_id == dog_id)
        .where(TrainingSession.date == day)
    ).all()
