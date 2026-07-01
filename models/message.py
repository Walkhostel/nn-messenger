from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), index=True)
    receiver_id = Column(Integer, ForeignKey("users.id"), index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)
