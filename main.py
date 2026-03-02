from Internet import Wifi
from machine import Pin
import requests
import json
import time

ledPin = Pin("LED", Pin.OUT)
wifi = Wifi()
address = wifi.getAddress()

print(f"Raspberry is already connected with address: {address}")
time.sleep(3)

while True:
    print("Hola mundo from microPython")
    ledPin.toggle()
    time.sleep(0.1)