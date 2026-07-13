# src/api/app.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.user import UserCreate, UserLogin
from models import User
from db.models import pwd_context

router = APIRouter()

@router.post("/register", status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Проверяем, существует ли пользователь с таким именем
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    # Хешируем пароль перед сохранением
    hashed_password = User.hash_password(user.password)

    # Создаем нового пользователя
    db_user = User(
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    ___ALLOWED_HTML_1___mit()
    db.refresh(db_user)

    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Находим пользователя по имени
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    # Проверяем пароль
    if not db_user.verify_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    return {"message": "Login successful"}
