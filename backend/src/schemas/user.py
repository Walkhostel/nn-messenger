# src/schemas/user.py
from pydantic import BaseModel, validator
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

    # Валидация длины пароля (если нужно)
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    is_active: bool
    created_at: str

    class Config:
        from_attributes = True
