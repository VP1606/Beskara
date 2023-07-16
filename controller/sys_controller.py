from controller.zone_controller import launch_zone, send_wss_stat
from configurator.manager import main_manager as manager
from configurator.manager import Zone

from concurrent.futures import ThreadPoolExecutor, as_completed
import asyncio
import websockets
import json

async def launch_threaded():
    await send_wss_stat(running=True)
    await asyncio.sleep(3)
    threads = []

    with ThreadPoolExecutor(max_workers=len(manager.zones)) as executor:
        for id in manager.zones:
            threads.append(executor.submit(launch_zone, id))
        for _ in as_completed(threads):
            print("Thread finished.")

    print(manager.zone_prg)
    await send_wss_stat(running=False)

asyncio.run(launch_threaded())