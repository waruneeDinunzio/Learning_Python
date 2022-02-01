# Lists
names = ["John", "Jeab", "Many", "Bob"]
names[0] = "Jon"
print(names[0])
print(names[-2])
print(names[0:3])  # return range of index 0 to 3 but not include 3

# List methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, -1)
print(numbers)
numbers.remove(-1)
print (numbers)
numbers.clear()  #get the error said 'list' object has no attribute 'clear' ??
print (numbers)
print(1 in numbers)  # return boolean value
print(len(numbers))  # .length

# Tuples is similar to list but can't change it. use ()
# only has index() and count() methods and megic methods for ex _add_(self,x)
num = (1, 2, 3, 3)
print(num.count(3))  # 2


