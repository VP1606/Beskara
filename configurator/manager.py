import json

class Zone:
    def __init__(self, raw) -> None:
        self.id = int(raw['id'])
        self.description = str(raw['desc'])
        self.gpio_valve = int(raw['gpio_valve'])
        self.gpio_flm = int(raw['gpio_flm'])
        self.max_pressure = float(raw['pressure_max_psi'])
        self.delivery_goal = float(raw['delivery_goal_l'])

class ZonePrg_Dict(dict):
    def __setitem__(self, __key: int, __value: float) -> None:
        # print("You are changing the value of {} to {}!!".format(__key, __value))
        return super(ZonePrg_Dict, self).__setitem__(__key, __value)


class ConfigManager:
    def __init__(self) -> None:
        raw_json = None
        with open('configurator/config.json', 'r') as config_f:
            raw_json = json.load(config_f)
            config_f.close()

        self.wss_address = str(raw_json["wss_address"])

        self.zones = {}
        self.zone_prg = ZonePrg_Dict()
        self.zone_prg["cmd"] = "beskara_mlds"

        _zones = raw_json['zones']
        for _zone in _zones:
            formed_zone = Zone(_zone)
            self.zones[formed_zone.id] = formed_zone
            self.zone_prg[formed_zone.id] = 0.0

    def get_zone(self, id: int):
        return self.zones[id]
    
    def get_longest_zone(self) -> int:
        max_key = max(self.zones, key=lambda k: self.zones[k].delivery_goal)
        return max_key

main_manager = ConfigManager()