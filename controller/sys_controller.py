from controller.zone_controller import launch_zone
from configurator.manager import main_manager as manager
from configurator.manager import Zone

from concurrent.futures import ThreadPoolExecutor, as_completed

def launch_threaded():
    threads = []
    verbose_id = manager.get_longest_zone()
    with ThreadPoolExecutor(max_workers=len(manager.zones)) as executor:
        for id in manager.zones:
            threads.append(executor.submit(launch_zone, id, verbose_id))
        for _ in as_completed(threads):
            print("Thread finished.")

    print(manager.zone_prg)

launch_threaded()