from Internet import Wifi
from HttpRequest import Request
from machine import UART
import time
import math

adcPin = machine.ADC(26)

wifi = Wifi()
address = wifi.getAddress()
print(f"Raspberry is already connected with address: {address}")

request = Request()
time.sleep(2)

# Ten seconds interval
interval = 10000
last_millis = 0

while True:
    current_millis = time.ticks_ms()
    
    if current_millis - last_millis >= interval:
        last_millis = current_millis
    
        try:
            current_time = request.getTime()
            current_date = request.getDate()
            analog_value = adcPin.read_u16()
            request_time = request.time
            print(f"Current date: {current_date} current time: {current_time} request time: {request_time} ms")
            
            current_trades = request.getActiveTrades()
            current_total = round(current_trades['current_total'], 2)
            print(f"Current total is: {current_total}")
            
        except Exception as err:
            print(f"An error ocurred: {err}")
        