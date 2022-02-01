# While loop
i = 1
while i <= 5:
    print(i * '*')  # Python can * string
    i += 1

numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# For Loops
for item in numbers:
    print(item)

# range() range function use with for loop

number = range(5)  # this is range index 0 to 4
number = range(5, 10)  # this's range from index 5 to 10
number = range(5, 10, 2)  # 1st para is 1st indexNumber, 2nd para is endIndex, 3rd para is skip 2
print(number)
# for number in range(5):
#     print(number)
# if __name__ == '__main__':

n = int(input("n: ").strip())
for number in range(1, 11):
    print(str(n) + " x " + str(number) + " = " + str(number * n))

