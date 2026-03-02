import urequests
import requests
import json

class Request:
    def send():
        url = "http://api.openweathermap.org/data/2.5/weather?q=merida&appid=192dbed2ac66d17d5f75780635e474fa"
        response = requests.get(url)
        return json.loads(response.text)
