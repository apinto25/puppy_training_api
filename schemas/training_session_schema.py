
from pydantic import BaseModel
from datetime import date


class TrainingSessionWrite(BaseModel):
    dog_id: int
    command_id: int
    date: date
    duration_minutes: float


class TrainingSessionRead(BaseModel):
    id: int
    dog_id: int
    command_id: int
    date: date
    duration_minutes: float

    class Config:
        from_attributes = True
