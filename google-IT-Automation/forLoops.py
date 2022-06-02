def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

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