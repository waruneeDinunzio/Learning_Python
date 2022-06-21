class Birds:
    color = ""
    number = 2
    def count(num):
        return num.number
bluejay = Birds()
bluejay.count()
print(bluejay.count())

class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "puple"

this_pun_is_for_you = Flower()

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(rose()) 