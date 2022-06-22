class Birds:
    color = ""
    number = 2
    def count(num):
        return num.number
bluejay = Birds()
bluejay.count()
print(bluejay.number)

class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "puple"

this_pun_is_for_you = Flower()

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))


# method in class
class Dog:
  name = "kevin"
  years = 0
  def speak(self):
    print("Wof Wof! I'm a dog name {}!".format(self.name))
  def dog_years(self):
    return self.years * 7

bob = Dog()
bob.name = "Bob"
bob.years = 2
bob.speak()
print(bob.dog_years())

class Person:
    def __init__(self, name):
        self.name = name    
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return print("hi, my name is {}".format(self.name)) 

# Create a new instance with a name of your choice
some_person = Person("Jeab") 

# Call the greeting method
some_person.greeting()

# This is example of defaut construtor
class Cat:
  def __init__(self):
    self.cat = "Meaw, Meaw!"
  def greeting(self):
    print(self.cat)
cuteCate = Cat()
cuteCate.greeting()

class Cats:
  def __init__(self,name, greeting):
    self.name = name
    self.greeting = greeting
  def greeting_cat(self):
    print("Cat's name " + str(self.name) + " says '" + str(self.greeting) + "'")
cute_cat = Cats("Garfild", "What's up?")
cute_cat.greeting_cat()

# docstring """"give the info you want to documented """"
class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
   # """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)