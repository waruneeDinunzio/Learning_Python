def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285
print(sum_squares(3)) # 0*0= 0, 1*1= 1, 2*2 = 4 so 0+1+4= 5

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# Nested for loops
def domino():
    for left in range(7):
        for right in range(left, 7):
            print("[" + str(left) + "|" + str(right) + "]", end=" ")
        print()
print(domino())   
# print()Function take second paramiter tobe a newline character

teams = ["Dragons", "Wolves", "Pandas", "Unicorns"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " VS " + away_team)  

# common pitfalls: Forgetting that the upperlimit of a range() isn't included
# : Iterating over non-sequences. integer numbers aren't iterable. String are iterable
def is_valid(user):
    if (len(user) > 3):
        return True
    else:
        return False

def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat"])  

# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
for x in range(1,11):
    print(x**3)

# Write a script that prints the multiples of 7 between 0 and 100. 
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7.
# Remember that 0 is also a multiple of 7.
# for n in range(101):
#     if(n%7 == 0):
#         print(n)

for x in range(1, 10, 3):
    print(x)


for x in range(10):
    for y in range(x):
        print(y)

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

votes(["Yes","No","Maybe"])