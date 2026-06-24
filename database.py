from sqlmodel import create_engine, Session
from typing import Generator
import os

DATABASE_URL = "sqlite:///messages.db"

engine = create_engine(DATABASE_URL, echo=False)

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

