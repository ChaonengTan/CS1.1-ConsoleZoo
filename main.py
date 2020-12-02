from Animal import Animal
from Monkey import Monkey
from Clownfish import Clownfish
from DickButt import DickButt

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
    def hollar(self):
        for animal in self.animals:
            print(animal.getSound())
    def addAnimal(self, animal):
        self.animals.append(animal)
    def removeAnimal(self, targetAnimal):
        for animal in self.animals:
            if animal.getName() == targetAnimal:
                print(f"{targetAnimal} has been purged")
                return
        print(f"Silly {targetAnimal} dosent exist")
        
        
zoo1=Zoo("yes")
champ1 = Monkey("champ1", "Male")
clown1 = Clownfish("clown1")
dickButt1 = DickButt("yes1")

zoo1.addAnimal(champ1)
zoo1.addAnimal(clown1)
zoo1.addAnimal(dickButt1)

zoo1.hollar()

print("Monkey **************************************************")
champ1.feed(420)
champ1.getBananas()
print(champ1.getButt())
print("ClownFish **************************************************")
zoo1.animals[1].getSpecies()
zoo1.animals[1].isSwimmingBackwards()
if zoo1.animals[1].getStatus():
    zoo1.removeAnimal("clown1")
print("DickButt **************************************************")
dickButt1.feed()
dickButt1.getGender()
dickButt1.getAge()
print(dickButt1.getButt())