from Animal import Animal
class Monkey(Animal):
    def __init__(self, name, gender, butt="hairy", bananas=0):
        super().__init__(name, gender, sound="Ooh Ohh Ahh Ahh")
        self.bananas = bananas
        self.butt = butt
    def feed(self, num=1):
        self.bananas += num
        print(f'{self.name} now has {self.bananas} bananas!')
    def getBananas(self):
        return (self.bananas)
    def getButt(self):
        return (self.butt)