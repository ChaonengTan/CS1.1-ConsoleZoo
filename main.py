from Components.Animal import Animal
from Components.Monkey import Monkey
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
    def hollar(self):
        for animal in self.animals:
            print(animal.getSound)
zoo1=Zoo("yes")
champ1 = Monkey("champ1", "Male")

zoo1.animals.append(champ1)