# Using recursion to implement power and factorial functions

# 5^3 = 5*5*5 = 125
def power(num, pwr):
    if pwr == 0: # this is a breaking statment!
        return 1
    else:
        return num * power(num,pwr-1)

# 4! = 4*3*2*1 = 24
# 0! = 1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * (factorial(num-1))


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
