from dataclasses import dataclass
from fastapi import WebSocket
import uuid
import json
import config_handler

@dataclass
class BarTender:
    def __init__(self) -> None:
        self.active_connections: dict = {}
        self.uuid_to_userid: dict = {}
        self.running_delivery = False

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        new_uuid = str(uuid.uuid4())
        self.active_connections[new_uuid] = websocket

    def disconnect(self, websocket: WebSocket):
        loc_uuid = self.find_connection_id(websocket)
        del self.active_connections[loc_uuid]

    def find_connection_id(self, websocket: WebSocket):
        locked_list = self.active_connections

        val_list = list(locked_list.values())
        key_list = list(locked_list.keys())

        loc_uuid = val_list.index(websocket)
        return key_list[loc_uuid]
    
    async def targeted_send_package(self, websocket: WebSocket, payload: json):
        await websocket.send_json(payload)

    async def broadcast_package(self, payload: json):
        for connection in self.active_connections.values():
            await connection.send_json(payload)

    async def main_switch(self, websocket: WebSocket, payload: dict):
        try:
            command = payload["cmd"]

            if command == "beskara_mlds":
                await self.broadcast_package(payload=payload)
            elif command == "beskara_mstat":
                self.running_delivery = bool(payload["running"])
                await self.broadcast_package(payload=payload)

            elif command == "bclient_get_config":
                if self.running_delivery:
                    print("Unavailable; running delivery.")
                else:
                    rep = config_handler.load_config()
                    await self.targeted_send_package(websocket=websocket, payload=rep)

            elif command == "bclient_set_config":
                if self.running_delivery:
                    print("Unavailable; running delivery.")
                else:
                    data = json.dumps(payload["data"])
                    config_handler.update_config(new_json=data)
                    rep = config_handler.load_config()
                    await self.targeted_send_package(websocket=websocket, payload=rep)

            else:
                print("Unrecognised command!")

        except KeyError:
            print("Unknown Key!")