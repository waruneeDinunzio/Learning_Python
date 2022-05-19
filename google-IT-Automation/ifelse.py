def format_name(first_name, last_name):
	# code goes here
	if(first_name== "" and last_name == ""):
		string = ""
	elif(first_name == ""):
		string = "Name: "+ last_name
	elif(last_name == ""):
		string = "Name: "+ first_name
	else:
		string = "Name: "+ last_name +", "+ first_name
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

# Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
		
	elif color == "green":
		hex_color = "#00ff00"
		
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown