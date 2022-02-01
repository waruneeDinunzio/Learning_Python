# Variables in Python is super easy don't have to use var or let
# or what data type? just write the name of variable for ex
age = 20
price = 19.95
first_name = "Jeab"  # 2 space for inline comment and use _ connect 2 words
is_online = True  # False True: capital the first letter



# birth_year = raw_input("Enter you birth year?")
# age = 2020 - int(birth_year)
# print(float(age))
# first = float(input("first number: "))
# second = float(input("second number: "))
# total = first + second
# print("Sum: " + str(total))

# Python has ''' ''' for muliple line for ex:
say = '''what's up!?
my name is Jeab
nice to meet you!!
'''
print(say)
# Python knows index in string begin with [0] and can take [-1]
print(say[0:10])
course = 'Python for beginners'
print(course.find('y'))
print(course.replace('for', '4'))
# this called "in" || "not in" operator. It'll return Boolean value
print("Python" not in course)

# Arithmetic Operators: ex + - * / %
# / => floating number, // => int (floor division)
# % return the remain of the division of numbers
# ** return the power of the number (Exponentiation) ex:
print(10 ** 3)
# ^ = 10 * 10 *10 = 1000
# Assignment Operators
# += ex> x = x+5 || x += 5
# Python is very good at math. it understand order of operation for ex:
print(10+3*2)

# Comparison operators
# == !== > >= < <=
x = 3 <= 3
print(x)

# Logical Operators
# and (both have to be true)
# or (at least one true)
# not (reverse)
price = 25
print(price > 10 and price < 30)
print(price > 30)
print(not price > 30)

temperature = 9
# Phthon use ident to identifile block code same as { } in JS
if temperature > 30:
    print("It's a hot day")
    print("drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("it's cold day")
print(temperature, "Done")
