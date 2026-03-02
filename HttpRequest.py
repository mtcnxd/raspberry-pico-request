import urequests
import requests
import json

class Request:
    def __init__():
        self.baseUrl="https://mecanicarubio.com/api"
    
    def getDateTime():
        url = f"{self.baseUrl}/sensors/time"
        response = requests.get(url)
        return json.loads(response.text)

    def to_celsius(degrees):
        data = float(degrees)
        return (data - 32.0)/1.8
