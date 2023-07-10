from configurator.manager import main_manager as manager
from configurator.manager import Zone
import time

import random

def demo_get_flm(port: int):
    return random.uniform(7800.0, 8000.0)

def demo_open_valve(port: int):
    print("VALVE {0} OPEN".format(port), end='\n')

def demo_close_valve(port: int):
    print("VALVE {0} CLOSED".format(port), end='\n')

def zone_control(id: int = 0):
    zone_det: Zone = manager.get_zone(id=id)
    delivered = 0.0

    demo_open_valve(port=zone_det.gpio_valve)
    time_cache = time.time()
    fl_cache = demo_get_flm(port=zone_det.gpio_flm)

    while delivered <= zone_det.delivery_goal:
        fl_now = demo_get_flm(port=zone_det.gpio_flm)
        fl_use = min(fl_now, fl_cache)
        time_now = time.time()

        delivered += (fl_use/60) * (time_now - time_cache)

        fl_cache = fl_now
        time_cache = time_now
        print('     {0} / {1} : {2}%'.format(round(delivered,3), round(zone_det.delivery_goal, 1), round(((delivered / zone_det.delivery_goal)*100), 2)), end='\r')

    demo_close_valve(port=zone_det.gpio_valve)

# zone_control(id=1)