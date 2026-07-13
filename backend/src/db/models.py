# src/db/models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from passlib.context import CryptContext

Base = declarative_base()

# Создаем контекст для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    # Убираем email из модели, как было согласовано
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Метод для хеширования пароля
    @classmethod
    def hash_password(cls, password: str) -> str:
        return pwd_context.hash(password)

    # Метод для проверки пароля
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)

    # Отношения (будут использоваться позже)
    # messages_sent = relationship("Message", back_populates="sender")
    # messages_received = relationship("Message", back_populates="recipient")
