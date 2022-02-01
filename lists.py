friends = ['Jo', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year: ', friend)

# Concatenating lists using +
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# sliced
slicing = c[:3]
slicing = c[1:5]
print(slicing)
# type()
# dir()  # give method of list
print(dir(a))
# append() : add new elements at the end of the list
# in : logical operators the return True or False
print(9 in a)  # is 9 in a list?


# sort() : sorted the list order
print(friends)
friends.sort()
print(friends)

# Built-in functions and lists
nums = [3, 41, 12, 9, 8, 79, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

# example function to get input number and find average number
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count += 1
average = total/count
print('Average: ', average)

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average: ', average)
