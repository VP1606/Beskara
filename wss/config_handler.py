import json
import os

def load_config():
    parent_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))
    json_file_path = os.path.join(parent_directory, "configurator", "config.json")

    raw_json = None
    with open(json_file_path, 'r') as config_f:
        raw_json = json.load(config_f)
        config_f.close()

    main_returner = {
        "cmd": "beskara_config_get",
        "data": raw_json
    }
    return main_returner

def update_config(new_json):
    parent_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))
    json_file_path = os.path.join(parent_directory, "configurator", "config.json")

    with open(json_file_path, 'w') as config_f:
        config_f.write(new_json)
        config_f.close()
    
    return