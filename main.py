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
    response = response['main']['temp_max']
    degrees = Request.to_celsius(float(response))
    print(f"Response microPython: {degrees}")
    ledPin.toggle()
    time.sleep(3)