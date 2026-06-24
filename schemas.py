from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class MessageCreate(BaseModel):
    receiver_id: int
    text: str

class MessageOut(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    text: str
    created_at: str
    is_read: bool

    class Config:
        from_attributes = True

