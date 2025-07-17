from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from sqlmodel import Session

from database import create_db_and_tables, get_session

from routers.dog_router import router as dog_router
from routers.command_router import router as command_router
from routers.training_session_router import router as training_session_router

@asynccontextmanager
async def lifespan(app):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
SessionDep = Annotated[Session, Depends(get_session)]

app.include_router(dog_router)
app.include_router(command_router)
app.include_router(training_session_router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
