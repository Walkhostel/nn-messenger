from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.user import UserCreate, UserLogin
from models import User

router = APIRouter()

@router.post("/register", status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Временно — просто заглушка
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Временно — просто заглушка
    return {"message": "Login successful"}
