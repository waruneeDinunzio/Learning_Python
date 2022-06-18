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
#'{:d}'.format(10.5) → '10'

# more examble of how to use .format()
def to_celsius(x):
    return (x-32)*5/9
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} c".format(x,to_celsius(x)))

# The format_address function separates out parts of the address string into new strings: 
# house_number and street_name, and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, 
# followed by the street name which may contain numbers, 
# but never by themselves, and could be several words long. 
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".
def format_address(address_string):
  # Declare variables
  address_split = address_string.split(" ",1)
  address_number = address_split[0]
  street_name = address_split[1]
  #print(address_split)
  # Separate the address string into parts
  
  # Traverse through the address parts
  #for __:
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(address_number,street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
