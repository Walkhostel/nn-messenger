from fastapi import APIRouter, WebSocket, Depends
from manager.connection import ConnectionManager

router = APIRouter()

manager = ConnectionManager()

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"User {user_id}: {data}", websocket)
    except:
        manager.disconnect(websocket)
