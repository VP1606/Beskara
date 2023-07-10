from controller.zone_controller import zone_control
from configurator.manager import main_manager as manager
from configurator.manager import Zone

from concurrent.futures import ThreadPoolExecutor, as_completed

def launch_threaded():
    threads = []
    with ThreadPoolExecutor(max_workers=len(manager.zones)) as executor:
        for id in manager.zones:
            threads.append(executor.submit(zone_control, id))
        for _ in as_completed(threads):
            print("Thread finished.")

launch_threaded()