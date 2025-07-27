from app.routers import ws_routes
from fastapi import FastAPI, WebSocket
from app.routers import analytics, metrics

app = FastAPI()

app.include_router(metrics.router)
app.include_router(analytics.router)
app.include_router(ws_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

# @app.websocket("/ws/live-data")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         await websocket.send_text("Live crypto price update!") 

