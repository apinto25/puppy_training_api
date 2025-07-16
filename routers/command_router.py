from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.command import Command
from schemas.command_schema import CommandCreate, CommandRead
from database import get_session


router = APIRouter(prefix="/commands", tags=["commands"])


@router.get("/", response_model=list[CommandRead])
def get_commands(session: Session = Depends(get_session)):
    commands = session.exec(select(Command)).all()
    return commands


@router.get("/{command_id}", response_model=CommandRead)
def get_command_by_id(command_id: int, session: Session = Depends(get_session)):
    command = session.get(Command, command_id)
    if not command:
        raise HTTPException(status_code=404, detail="Command not found")
    return command


@router.post("/", status_code=201, response_model=CommandRead)
def create_command(command: CommandCreate, session: Session = Depends(get_session)):
    db_command = Command.model_validate(command)
    session.add(db_command)
    session.commit()
    session.refresh(db_command)
    return db_command


@router.delete("/{command_id}", status_code=204)
def delete_command(command_id: int, session: Session = Depends(get_session)):
    command = session.get(Command, command_id)
    if not command:
        raise HTTPException(status_code=404, detail="Command not found")
    session.delete(command)
    session.commit()
    return None
