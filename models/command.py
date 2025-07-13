from sqlmodel import SQLModel, Field

class Command(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str

    def __repr__(self):
        return f"Command(id={self.id}, name='{self.name}', description='{self.description}', is_active={self.is_active})"
