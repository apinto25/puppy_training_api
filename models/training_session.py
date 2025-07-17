
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date


class TrainingSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    dog_id: int = Field(foreign_key="dog.id")
    command_id: int = Field(foreign_key="command.id")
    date: date
    duration_minutes: float
