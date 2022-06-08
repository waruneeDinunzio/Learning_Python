# Formatting
def student_grade(name, grade):
	return ("{} received {}% on the exam").format(name,grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""
# "{var1} {var2}".format(var1=value1, var2=value2)
#"{:exp1} {:exp2}".format(value1, value2)
# {:d} integer value
'{:d}'.format(10.5) → '10'

# more examble of how to use .format()
def to_celsius(x):
    return (x-32)*5/9
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} c".format(x,to_celsius(x)))

