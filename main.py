from Internet import Wifi
from HttpRequest import Request
from machine import Pin
import time

ledPin = Pin("LED", Pin.OUT)

wifi = Wifi()
address = wifi.getAddress()

print(f"Raspberry is already connected with address: {address}")
time.sleep(3)

while True:
    response = Request.send()
    print(f"Hola mundo from microPython: {response}")
    ledPin.toggle()
    time.sleep(0.5)