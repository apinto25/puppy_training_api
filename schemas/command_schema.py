from pydantic import BaseModel


class CommandCreate(BaseModel):
    name: str
    description: str
    

class CommandRead(BaseModel):
    id: int
    name: str
    description: str
    
    class Config:
        orm_mode = True
