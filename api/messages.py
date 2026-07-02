from fastapi import APIRouter, Depends, WebSocket
from sqlalchemy.orm import Session
from ___ALLOWED_HTML_3___ssage import Message
from models.user import User
from database.database import SessionLocal
from websocket.manager import ConnectionManager
from auth.utils import verify_password
from typing import List

router = APIRouter()
ws_manager = ConnectionManager()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/send")
def send_message(sender_id: int, receiver_id: int, text: str, db: Session = Depends(get_db)):
    message = Message(sender_id=sender_id, receiver_id=receiver_id, text=text)
    db.add(message)
    ___ALLOWED_HTML_4___mit()
    db.refresh(message)

    # Уведомляем получателя через WebSocket
    ws_manager.broadcast(
        {"type": "message", "id": message.id, "sender_id": sender_id, "text": text, "is_read": False},
        exclude=receiver_id  # Не отправляем самому себе (если нужно)
    )

    return {"status": "sent", "message_id": message.id}

@router.get("/history")
def get_history(sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    messages = db.query(Message).filter(
        ((Message.sender_id == sender_id) & (Message.receiver_id == receiver_id)) |
        ((Message.sender_id == receiver_id) & (Message.receiver_id == sender_id))
    ).order_by(Message.created_at).all()

    return [
        {
            "id": msg.id,
            "sender_id": msg.sender_id,
            "receiver_id": msg.receiver_id,
            "text": msg.text,
            "created_at": msg.created_at.isoformat(),
            "is_read": msg.is_read
        }
        for msg in messages
    ]
