import network

class Wifi:
    def __init__(self):
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)
        self.sta_if.connect('SMARTHOME','100%smart')

        while (self.sta_if.isconnected == False):
            print("Connecting to wlan")
            time.sleep(1)
    
    def getAddress(self):
        return self.sta_if.ifconfig()[0]