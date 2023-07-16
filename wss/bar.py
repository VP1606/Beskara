from fastapi import FastAPI, WebSocket, WebSocketDisconnect, WebSocketException
import bartender as BT

app = FastAPI()
manager = BT.BarTender()

@app.websocket("/wss")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            print(data)
            # await websocket.send_text(f"Message text was: {data}")
            await manager.broadcast_package(payload=data)

    except:
        manager.disconnect(websocket=websocket)