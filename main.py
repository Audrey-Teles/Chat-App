# API imports
from fastapi import FastAPI
import uvicorn

# My imports
from socketManager import SocketManager
from routers.users import router as router_user
from routers.websockets import router as router_websocket
from routers.chat import router as router_chat

# instances
app = FastAPI()
manager = SocketManager()

# Add user endpoints to API
app.include_router(router_user)
app.include_router(router_websocket)
app.include_router(router_chat)

if __name__ == '__main__':
    uvicorn.run(app, port=8080)

