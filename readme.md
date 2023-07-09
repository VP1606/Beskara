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