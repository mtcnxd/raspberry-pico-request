import requests
import json

class Request:
    def __init__(self):
        self.baseUrl="https://mecanicarubio.com/api"
        self.response = None
        
    def refreshDateTime(self):
        url=f"{self.baseUrl}/sensors/time"
        response = requests.get(url)
        self.response = json.loads(response.text)
        
    def parseTime(self):
        if self.response == None:
        	self.refreshDateTime()        
        return self.response['time']
        
    def parseDate(self):
        if self.response == None: 
        	self.refreshDateTime()
        return self.response['date']
        