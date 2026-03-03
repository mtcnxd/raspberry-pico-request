from Internet import Wifi
from HttpRequest import Request
from machine import Pin
import time

ledPin = Pin("LED", Pin.OUT)

wifi = Wifi()
request = Request()
address = wifi.getAddress()

print(f"Raspberry is already connected with address: {address}")
time.sleep(2)

while True:
    request.refreshDateTime()    
    current_time = parse.getTime()
    current_date = parse.getDate()
    
    print(f"Current date: {current_date} current time: {current_time}")
    ledPin.toggle()
    time.sleep(5)