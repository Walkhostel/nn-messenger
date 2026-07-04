from fastapi import FastAPI
from api import router as api_router
from db import init_db
from utils.logging import setup_logging

app = FastAPI(title="Chat Backend", description="Simple chat backend with WebSocket support", version="1.0.0")

# Инициализация логгера
setup_logging()

# Инициализация базы данных
init_db()

# Подключение API-роутеров
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Chat backend is running"}
