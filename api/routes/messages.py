from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from models import Message, User
from schemas import MessageCreate, MessageOut
from typing import List
from utils.security import decode_jwt_token
from uuid import uuid4
import json

router = APIRouter()

@router.get("/history")
def get_message_history(
    other_user_id: int,
    current_user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
 
    messages = (
        db.query(Message)
        .filter(
            (Message.sender_id == current_user_id) & (Message.receiver_id == other_user_id)
            | (Message.sender_id == other_user_id) & (Message.receiver_id == current_user_id)
        )
        .order_by(Message.created_at)
        .all()
    )

    return [MessageOut.model_validate(message) for message in messages]


@router.post("/send")
def send_message(
    message_data: MessageCreate,
    current_user_id: int,
    db: Session = Depends(get_db)
):
    receiver = db.query(User).filter(User.id == message_data.receiver_id).first()
    if not receiver:
        raise HTTPException(status_code=404, detail="Получатель не найден")

    sender = db.query(User).filter(User.id == current_user_id).first()
    if not sender:
        raise HTTPException(status_code=404, detail="Отправитель не найден")
      
    new_message = Message(
        sender_id=current_user_id,
        receiver_id=message_data.receiver_id,
        text=message_data.text,
        is_read=False
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
  
    return MessageOut.model_validate(new_message)
