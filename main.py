from fastapi import FastAPI
from database.database import init_db
from auth.routes import router as auth_router
from websocket.manager import ConnectionManager
from ___ALLOWED_HTML_0___ssages import router as messages_router

app = FastAPI(title="Messenger MVP")

# Инициализация БД
init_db()

# Подключение маршрутов
app.include_router(auth_router, prefix="/auth")
app.include_router(messages_router, prefix="/api")

# Подключение WebSocket-менеджера
ws_manager = ConnectionManager()

# Событие запуска
@app.on_event("startup")
def startup_event():
    print("Сервер запущен. Ожидание подключений...")
