from configurator.manager import main_manager as manager
from configurator.manager import Zone
import time

import random
import websockets
import asyncio
import json

def demo_get_flm(port: int):
    return random.uniform(7800.0, 8000.0)

def demo_open_valve(port: int):
    print("VALVE {0} OPEN".format(port), end='\n')

def demo_close_valve(port: int):
    print("VALVE {0} CLOSED".format(port), end='\n')

async def zone_control(id: int, websocket):
    await websocket.send(json.dumps(manager.zone_prg))
    zone_det: Zone = manager.get_zone(id=id)
    delivered = 0.0
    manager.zone_prg[id] = 0.0

    demo_open_valve(port=zone_det.gpio_valve)
    time_cache = time.time()
    fl_cache = demo_get_flm(port=zone_det.gpio_flm)

    start_time = time.time()
    count = 0

    while delivered <= zone_det.delivery_goal:
        fl_now = demo_get_flm(port=zone_det.gpio_flm)
        fl_use = min(fl_now, fl_cache)
        time_now = time.time()

        delivered += (fl_use/60) * (time_now - time_cache)
        manager.zone_prg[id] = delivered

        fl_cache = fl_now
        time_cache = time_now
        count += 1

    demo_close_valve(port=zone_det.gpio_valve)

    frequency = float(count) / (time.time() - start_time)
    frequency = round(frequency, 3)
    print("ZONE {0} DONE: {1} / {2} at {3} Hz".format(id, round(delivered, 2), round(zone_det.delivery_goal, 2), frequency))
    await websocket.send(json.dumps(manager.zone_prg))

async def zone_control_loop(id: int, verbose: bool):
    async with websockets.connect('ws://127.0.0.1:8000/wss') as websocket:
            await zone_control(id, websocket)
            print("ZC COMP")
            await websocket.close()

def launch_zone(id: int, verbose_id):
    verbose = False
    if id == verbose_id:
        verbose = True
    asyncio.run(zone_control_loop(id=id, verbose=verbose))