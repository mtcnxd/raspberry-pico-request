import network

class Wifi:
    def __init__(self):
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)
        self.sta_if.connect('INFINITUM3E81_2.4','Lg5Bz8Kf4v')

        while (self.sta_if.isconnected == False):
            time.sleep(1)
    
    def getAddress(self):
        return self.sta_if.ifconfig()[0]