from Animal import Animal
from mixIns import getButtMixin
import random

class DickButt(Animal, getButtMixin):
    def __init__(self, name, butt="Hairy"):
        super().__init__(name, gender="Nope", sound="*fart")
        self.age = random.randint(0,70)
        self.butt = butt
    def feed(self):
        print("Silly~ DickButts dont eat!")
    def getGender(self):
        print("Silly~ Its a DickButt")
    def getAge(self):
        print(f"{self.name} is {self.age} years old!")
        if self.age > 50:
            print(f"Woah! {self.name} is a Great Sage!")
        elif (self.age > 30):
            print(f"Woah! {self.name} is a Wizard!")