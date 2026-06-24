# main.py
from fastapi import FastAPI
from database import engine
from models import Base
from api.routes import auth, messages, websocket
import uvicorn

#таблицы в БД
Base.metadata.create_all(bind=engine)

#приложение
app = FastAPI(title="Мессенджер — MVP", description="Локальный текстовый чат между двумя пользователями", version="0.1.0")

# Подключаем маршруты
app.include_router(auth.router, prefix="/auth", tags=["Авторизация"])
app.include_router(messages.router, prefix="/messages", tags=["Сообщения"])
app.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])

#корневой маршрут
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в мессенджер! Используйте /docs для просмотра API."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

