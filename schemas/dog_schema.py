from pydantic import BaseModel
from typing import Optional
from datetime import date


class DogCreate(BaseModel):
    name: str
    breed: str
    birth_date: date
    

class DogRead(BaseModel):
    id: int
    name: str
    breed: str
    birth_date: date
