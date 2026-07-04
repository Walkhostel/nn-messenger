from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router

# Создаём приложение
app = FastAPI(title="Chat Backend", version="1.0.0")

# Настройка CORS (временно разрешаем всё)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

# Простой endpoint для проверки
@app.get("/")
def health_check():
    return {"status": "OK", "message": "Backend is running"}
