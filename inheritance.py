class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, paraName):
        self.name = paraName
        print(self.name, "constructed")

    def party(self):
        self.x = self.x +1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points +7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally") # Sally constructed
s.party() # Sally party count 1

j = FootballFan("jim") # jim constructed and jim partry count 1(on line 16 so x = 1)
j.party() # jim party count 2
j.touchdown() # jim points 7