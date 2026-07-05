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

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await ___ALLOWED_HTML_0___nnect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"User {user_id}: {data}", websocket)
    except:
        manager.disconnect(websocket)
