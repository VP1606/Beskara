import json

class Zone:
    def __init__(self, raw) -> None:
        self.id = int(raw['id'])
        self.description = str(raw['desc'])
        self.gpio_valve = int(raw['gpio_valve'])
        self.gpio_flm = int(raw['gpio_flm'])
        self.max_pressure = float(raw['pressure_max_psi'])
        self.delivery_goal = float(raw['delivery_goal_l'])


class ConfigManager:
    def __init__(self) -> None:
        raw_json = None
        with open('configurator/config.json', 'r') as config_f:
            raw_json = json.load(config_f)
            config_f.close()

        self.zones = {}
        _zones = raw_json['zones']
        
        for _zone in _zones:
            formed_zone = Zone(_zone)
            self.zones[formed_zone.id] = formed_zone

    def get_zone(self, id: int):
        return self.zones[id]

main_manager = ConfigManager()