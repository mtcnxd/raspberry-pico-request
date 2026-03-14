from Internet import Wifi
from HttpRequest import Request
import time

<<<<<<< HEAD
ledPin = Pin("LED", Pin.OUT)
=======
>>>>>>> 005a527 (Datalog in pico W)
adcPin = machine.ADC(26)

wifi = Wifi()
address = wifi.getAddress()
print(f"Raspberry is already connected with address: {address}")

request = Request()
time.sleep(2)

<<<<<<< HEAD
print(f"Raspberry is already connected with address: {address}")
time.sleep(3)

interval = 1000
last_millis = 0
seconds = 0
=======
# Ten seconds interval
interval = 10000
last_millis = 0
>>>>>>> 005a527 (Datalog in pico W)

while True:
    current_millis = time.ticks_ms()
    
    if current_millis - last_millis >= interval:
        last_millis = current_millis
<<<<<<< HEAD
        seconds = seconds + 1
        print(f"Seconds {seconds}")
        ledPin.toggle()
    
    if seconds >= 10:
=======
    
>>>>>>> 005a527 (Datalog in pico W)
        try:
            current_time = request.getTime()
            current_date = request.getDate()
            analog_value = adcPin.read_u16()
<<<<<<< HEAD
            print(f"Current date: {current_date} current time: {current_time} seconds: {seconds} value: {analog_value}")
            seconds = 0
        except Exception as e:
            print(f"Error: {e}")
=======
            request_time = request.time
            print(f"Current date: {current_date} current time: {current_time} request time: {request_time} ms")
            
        except Exception as e:
            print(f"An error ocurred: {e}")
>>>>>>> 005a527 (Datalog in pico W)
        