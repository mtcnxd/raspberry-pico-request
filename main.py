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

interval = 5000
last_millis = 0
five_seconds = 0

while True:
    current_millis = time.ticks_ms()
    
    if current_millis - last_millis >= interval:
        print(current_millis - last_millis)
        last_millis = current_millis
        five_seconds = five_seconds + 1
    else:
        ledPin.toggle()
    
    if five_seconds >= 2:
        current_time = request.getTime()
        current_date = request.getDate()        
        print(f"Current date: {current_date} current time: {current_time} seconds: {five_seconds}")
        five_seconds = 0
        