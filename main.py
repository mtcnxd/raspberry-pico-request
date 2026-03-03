from Internet import Wifi
from HttpRequest import Request
from machine import Pin
import time

ledPin = Pin("LED", Pin.OUT)

wifi = Wifi()
address = wifi.getAddress()

request = Request()

print(f"Raspberry is already connected with address: {address}")
time.sleep(3)

while True:    
    current_time = request.getTime()
    current_date = request.getDate()
    
    print(f"Current date: {current_date} current time: {current_time}")
    ledPin.toggle()
    time.sleep(3)