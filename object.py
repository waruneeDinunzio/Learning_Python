# def is the keyword for defining a function
# dir() is builtin function in python3 to returns list of attributes and methods of any object
# type(object) is return object's type
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal().party()
print("Type", type(an))
print("Dir", dir(an))
#__add__ = internal method for phthon
## Try dir() with a string

y = "hello world"
dir(y)
