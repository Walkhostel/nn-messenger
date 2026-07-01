from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

from models import Base
from config import DATABASE_URL

# Создаём движок
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаём сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Инициализация таблиц
def init_db():
    ___ALLOWED_HTML_1___tadata.create_all(bind=engine)
