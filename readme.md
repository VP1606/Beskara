# Beskara
A (soon to be) Smart Irrigation System written in Python.

## Layers

- WebSocket-powered connection layer (fastAPI).

- Local logic controller (in charge of controlling valves + telemetry report).

- Metal Interface: operations/functions to directly control valves via GPIO, and collect telemetry from flow meters and other components.

### Outgoing

- Valve status (open/closed)
- Flow rate
- Pressure (derived)
- Amount of water delivered during the session
- Percentage completed

### Incoming

- Valve shut off *(override)* and pause
- Delivery amount adjustment (per zone)
- Reset system fully

## To Run

Use the -m flag when running and execute the modules as scripts to allow parallel module support.

```py
python -m configurator.manager
```

## Virtual Environment

**DO NOT PUSH** any venv folders and files.

Use the name **"venv"** for your virtual environment.

Update requirements at the end of your feature, **after** merging into develop.

To install/create the venv:
```sh
python3 -m venv ./venv
```

To install required packages:
```sh
pip install -r requirements.txt
pip install pipreqs
```

To update requirements:
```sh
pipreqs --force
```