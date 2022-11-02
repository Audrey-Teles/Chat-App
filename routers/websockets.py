# Api imports
from fastapi import WebSocket
from fastapi import APIRouter
from fastapi import WebSocketDisconnect

# My imports
from socketManager import SocketManager

router = APIRouter(
    tags=["websocket"],
    responses={404: {"description": "Not found"}},
)
manager = SocketManager()


@router.websocket("/api/chat")
async def chat(websocket: WebSocket):
    # Check to se if users is registered/authenticated by reading from browser coockie
    sender = websocket.cookies.get("X-Authorization")
    if sender:
        # Connect user to websocket
        await manager.connect(websocket, sender)
        response = {
            "sender": sender,
            "message": "entrou no chat"
        }
        await manager.broadcast(response)

        try:
            while True:
                # Get data from connected user and broadcast it to all connected users
                data = await websocket.receive_json()
                await manager.broadcast(data)
        except WebSocketDisconnect:
            manager.disconnect(websocket, sender)
            response['message'] = "saiu"
            await manager.broadcast(response)
