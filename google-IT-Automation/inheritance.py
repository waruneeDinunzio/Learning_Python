class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

# other example
class Animal:
     sound = ""
     def __init__(self, name):
         self.name = name
     def speak(self):
         print("{sound} I'm {name}! {sound}".format(
             name=self.name, sound=self.sound))
 
class Piglet(Animal):
     sound = "Oink!"
 
class Cow(Animal):
     sound = "Moooo"
hamlet = Piglet("Hamlet")
hamlet.speak()
# Oink! I'm Hamlet! Oink! 
class Cow(Animal):
     sound = "Moooo"
 
milky = Cow("Milky White")
milky.speak()
# Moooo I'm Milky White! Moooo