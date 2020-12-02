from Animal import Animal
from mixIns import getButtMixin

class Monkey(Animal, getButtMixin):
    def __init__(self, name, gender, butt="hairy"):
        super().__init__(name, gender, sound="Ooh Ohh Ahh Ahh")
        self.bananas = 0
        self.butt = butt
    def feed(self, num=1):
        self.bananas += num
        print(f'{self.name} now has {self.bananas} bananas!')
    def getBananas(self):
        print(f'{self.name} has {self.bananas} bananas!')
        return (self.bananas)