from Animal import Animal
import random

class Clownfish(Animal):
    def __init__(self, name, species=random.choice([True, False])):
        super().__init__(name, gender="Male", sound="Blub Blub")
        self.rareSpecies = species
        self.swimBackwards = False
        self.dead = False
    def changeGender(self):
        if self.gender == "Male":
            self.gender = "Female"
        else:
            print(f"{self.name} has already turned Female")
    def getSpecies(self):
        if self.rareSpecies == True:
            print(f"{self.name} is of a rare species")
            return (True)
        else:
            print(f"{self.name} is not of a rare species")
            return (False)
    def getStatus(self):
        return (self.dead)
    def isSwimmingBackwards(self):
        self.swimBackwards = True
        if random.choice([True, False]):
            self.dead = True
            print(f"{self.name} encountered a fatal disease and died")
        else:
            print(f"Huh... interesting, {self.name} is swimming backwards...")

    # override instance
    def getGender(self):
        if self.gender == "Male":
            print(f"As of now {self.name}'s gender is {self.gender} but it may change")
            return ("Male")
        else:
            print(f"{self.name} is a Female")
            return ("Female")