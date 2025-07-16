from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date


class Dog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    breed: str
    birth_date: date
