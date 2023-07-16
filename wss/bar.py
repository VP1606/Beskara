from fastapi import FastAPI, WebSocket
import bartender as BT

app = FastAPI()
manager = BT.BarTender()

@app.websocket("/wss")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    while True:
        data = await websocket.receive_text()
        print(data)
        # await websocket.send_text(f"Message text was: {data}")