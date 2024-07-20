from gpiozero import OutputDevice, InputDevice ## Deprecate!
import RPi.GPIO as GPIO

def setup():
    print("Setup GPIO ports")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)

def open_valve(gpio_port):
    GPIO.output(16, GPIO.HIGH)
    print(f"Opened valve on GPIO port {gpio_port}")

def close_valve(gpio_port):
    GPIO.output(16, GPIO.LOW)
    print(f"Closed valve on GPIO port {gpio_port}")

def read_flm(gpio_port):
    flow_meter = InputDevice(gpio_port)
    flow_value = OutputDevice(gpio_port) 

    print(f"Reading flow meter on GPIO port {gpio_port}")
    return flow_value

setup()

# Hello this is angellou, I am gonna do DEZ commands on the UBUNTU server  
#sudo apt update
#sudo pip install gpiozero
#pip install gpiozero
#sudo apt install python3-pip