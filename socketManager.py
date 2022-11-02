from fastapi import WebSocket
from typing import List


# manager
class SocketManager:
    def __init__(self):
        self.activate_conections: List[(WebSocket, str)] = []

    # Connect users to websocket
    async def connect(self, websocket: WebSocket, user: str):
        await websocket.accept()
        self.activate_conections.append((websocket, user))

    # Disconnect/Remove users
    def disconnect(self, websocket: WebSocket, user: str):
        self.activate_conections.remove((websocket, user))

    # Send messages toa ll the connected users
    async def broadcast(self, data):
        for connection in self.activate_conections:
            await connection[0].send_json(data)
