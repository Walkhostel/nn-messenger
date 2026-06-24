from sqlmodel import SQLModel, Field, Column, DateTime, Integer, String
from datetime import datetime
from typing import Optional

class TimestampBase(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(DateTime(timezone=True)))

class User(TimestampBase, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    password_hash: str

class Message(TimestampBase, table=True):
    __tablename__ = "messages"

    id: Optional[int] = Field(default=None, primary_key=True)
    sender_id: int = Field(foreign_key="users.id")
    receiver_id: int = Field(foreign_key="users.id")
    text: str
    is_read: bool = False

