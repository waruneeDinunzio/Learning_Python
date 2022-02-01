# A Definite Loop with Strings for example: for loop
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year: ', friend)
print('Done')

# Finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12,3,74,15]:
    if the_num > largest_so_far:  # if-block
        largest_so_far = the_num  # end if-block
    print(largest_so_far, the_num)  # so it's printing this line every time in loops
print('After', largest_so_far)

# Finding the smallest number
smallest = None  # None is None (special)type of data
print("Before:", smallest)
for itervar in [41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break  #  ""break" stop at first loop so it's never loop
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

# Counting in a loop and adding in loops
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)

# Filtering in a loop
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')

# Search Using a Boolean variable
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

# Looping through strings. the shorter code the better!!
fruit = 'banana'
for letter in fruit:
    print(letter)

# using a While loop go thought a string

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

