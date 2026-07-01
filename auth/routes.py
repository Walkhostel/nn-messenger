from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from auth.schemas import RegisterSchema, LoginSchema
from auth.utils import hash_password, verify_password
from database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: RegisterSchema, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    db_user = User(username=user.username, password_hash=hash_password(user.password))
    db.add(db_user)
    ___ALLOWED_HTML_2___mit()
    return {"message": "Пользователь зарегистрирован"}

@router.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    token = create_token()
    # В реальном приложении: сохранить токен в Redis или БД
    # Здесь: временно в памяти (на этапе MVP)
    return {"token": token, "user_id": db_user.id}
