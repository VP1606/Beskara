from gpiozero import OutputDevice, InputDevice

def open_valve(gpio_port):
    valve = OutputDevice(gpio_port)
    valve.on()
    print(f"Opening valve on GPIO port {gpio_port}")

def close_valve(gpio_port):
    valve = OutputDevice(gpio_port)
    valve.off()
    print(f"Closing valve on GPIO port {gpio_port}")

def read_flm(gpio_port):
    flow_meter = InputDevice(gpio_port)
    flow_value = OutputDevice(gpio_port) 

    print(f"Reading flow meter on GPIO port {gpio_port}")
    return flow_value


# Hello this is angellou, I am gonna do DEZ commands on the UBUNTU server  
#sudo apt update
#sudo pip install gpiozero
#pip install gpiozero
#sudo apt install python3-pip