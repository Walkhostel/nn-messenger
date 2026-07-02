from typing import List
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.user_connections: dict = {}  # {user_id: websocket}

    async def connect(self, websocket: WebSocket, user_id: int):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.user_connections[user_id] = websocket

    def disconnect(self, websocket: WebSocket, user_id: int):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        if user_id in self.user_connections:
            del self.user_connections[user_id]

    async def broadcast(self, message: dict, exclude: int = None):
        """Отправка сообщения всем, кроме указанного пользователя"""
        for connection in self.active_connections:
            if exclude is None or connection != self.user_connections.get(exclude):
                await connection.send_json(message)

    async def send_to_user(self, user_id: int, message: dict):
        if user_id in self.user_connections:
            await self.user_connections[user_id].send_json(message)
