class SmartHome:
    def __init__(self, device_name):
        self.device_name = device_name



class Light(SmartHome):
    def __init__(self, device_name):
        super().__init__(device_name)

    def turn_on(self):
        #print(f"{self.device_name}")
        print("Light turned on")

class Speaker(SmartHome):
    def __init__(self, device_name):
        super().__init__(device_name)

    def turn_on(self):
        #print(f"{self.device_name} ")
        print("Speaker turned on")
class _SecurityCamera(SmartHome):
    def __init__(self, device_name):
        super().__init__(device_name)

    def turn_on(self):
        #print(f"{self.device_name} ")       
        print("Security camera turned on")

# devices = Light("Light turned on")
# devices = Speaker("Speaker Started")
# devices = _SecurityCamera("Security camera turned on")
devices = [
    Light("Light turned on"),        
    Speaker("Speaker Started"),
    _SecurityCamera("cemera recording")]


for device in devices:
    device.turn_on()
        