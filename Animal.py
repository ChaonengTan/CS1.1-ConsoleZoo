from abc import ABC

class Animal(ABC):
    def __init__(self, name, gender, sound):
        self.name = name
        self.gender = gender
        self.sound = sound
    def getName(self):
        return(self.name)
    def getGender(self):
        return(self.gender)
    def getSound(self):
        return(self.sound)
