import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    print(kwargs)
    # {'bule':4, 'red': 2, 'green':6}
    for key, value in kwargs.items():
      for i in range(value): # i = 4 for first item
        self.contents.append(key) # append bule 4 time
    print(self.contents)

  def draw(self, number):
    all_removed = []
    if(number > len(self.contents)):
      return self.contents
    for i in range(number):
      removed = self.contents.pop(int(random.random()*len(self.contents)))
      all_removed.append(removed)
    return all_removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#   M = 0
#   for i in range(num_experiments):
#     hat_copy = copy.deepcopy(hat)
#     balls = hat_copy.draw(num_balls_drawn)

#     eb_list = []
#     for k, v in expected_balls.items():
#       eb_list += v * [k]

#     if contains_balls(eb_list, balls):
#       M +=1
  

#   return M / num_experiments

# def contains_balls(exptected_balls, actual_balls):
#   for b in exptected_balls:
#     if b in actual_balls:
#       actual_balls.remove(b)
#     else:
#       return False
#   return True

  M = 0
  for i in range(num_experiments):
      expected_copy = copy.deepcopy(expected_balls)
      hat_copy = copy.deepcopy(hat)
      colors_gotten = hat_copy.draw(num_balls_drawn)

      for color in colors_gotten:
          if(color in expected_copy):
              expected_copy[color] -= 1

      if(all(x <= 0 for x in expected_copy.values())):
            M += 1
  return M / num_experiments