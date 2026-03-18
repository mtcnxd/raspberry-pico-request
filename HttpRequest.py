from Exceptions import RuntimeExeption
from machine import Pin
from Datalog import Datalog
import requests
import json
import time

class Request:
    def __init__(self):
        self.ledPin = Pin("LED", Pin.OUT)
        self.baseUrl="https://mecanicarubio.com/api"
        self.response = ""
        self.time = 0
        
    def getDateTime(self):
        url=f"{self.baseUrl}/sensors/time"
        self.ledPin.on()
        start_time = time.ticks_ms()
        response = requests.get(url)
        end_time = time.ticks_ms()
        self.ledPin.off()
        self.time = end_time - start_time
        if self.time > 2000:
            Datalog.write(f"Time exceeded: {self.time} ms")
            raise RuntimeExeption(f"Request time exceeded: {self.time} ms")

        if response is None:
            raise RuntimeExeption("Can't get the requested information")
        
        self.response = json.loads(response.text)
        
    def getTime(self):
        self.getDateTime()
        return self.response['time']
        
    def getDate(self):
        self.getDateTime()
        return self.response['date']
    
    def getActiveTrades(self):
        url=f"{self.baseUrl}/sensors/trades"
        response = requests.get(url)
        return json.loads(response.text)

        