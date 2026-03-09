from Internet import Wifi
from HttpRequest import Request
from machine import Pin
import time

ledPin = Pin("LED", Pin.OUT)
adcPin = machine.ADC(26)

wifi = Wifi()
address = wifi.getAddress()

request = Request()

print(f"Raspberry is already connected with address: {address}")
time.sleep(3)

interval = 1000
last_millis = 0
seconds = 0

while True:
    current_millis = time.ticks_ms()
    
    if current_millis - last_millis >= interval:
        last_millis = current_millis
        seconds = seconds + 1
        print(f"Seconds {seconds}")
        ledPin.toggle()
    
    if seconds >= 10:
        try:
            current_time = request.getTime()
            current_date = request.getDate()
            analog_value = adcPin.read_u16()
            print(f"Current date: {current_date} current time: {current_time} seconds: {seconds} value: {analog_value}")
            seconds = 0
        except Exception as e:
            print(f"Error: {e}")
        