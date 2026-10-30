
from abc import ABC, abstractmethod

# Abstract parent class
class SmartDevice(ABC):

    def __init__(self, device_name):
        self.device_name = device_name

    @abstractmethod
    def operate(self):
        pass


# Child class 1
class SmartLight(SmartDevice):

    def operate(self):
        print(self.device_name, "is turning ON. Lights are glowing!")


# Child class 2
class SmartFan(SmartDevice):

    def operate(self):
        print(self.device_name, "is turning ON. Fan is rotating!")


# Child class 3
class SmartSpeaker(SmartDevice):

    def operate(self):
        print(self.device_name, "is playing music!")


# Creating objects
light = SmartLight("Living Room Light")
fan = SmartFan("Bedroom Fan")
speaker = SmartSpeaker("Smart Speaker")

# Storing devices in a list
devices = [light, fan, speaker]

# Using polymorphism
print("Welcome to Smart Device Command Center!")

for device in devices:
    device.operate()
