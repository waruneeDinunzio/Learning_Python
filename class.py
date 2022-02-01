# __init__ =
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z): # z = parameter input
        self.name = z
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy') # Quincy is constructed

m = PartyAnimal('Miya') # Miya is constructed/created

q.party()
m.party()
q.party()
q = 40
# q object change value to 40 (disccarded)
print(q)
# q.party()
# q.party() not exit anymore