from Internet import Wifi
from HttpRequest import Request
import time

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
            
        except Exception as e:
            print(f"An error ocurred: {e}")
        