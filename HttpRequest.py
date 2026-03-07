import requests
import json

class Request:
    def __init__(self):
        self.baseUrl="https://mecanicarubio.com/api"
        self.response = ""
        
    def getDateTime(self):
        url=f"{self.baseUrl}/sensors/time"
        response = requests.get(url)
        self.response = json.loads(response.text)
        
    def getTime(self):
        self.getDateTime()
        return self.response['time']
        
    def getDate(self):
        self.getDateTime()
        return self.response['date']
        