from operator import le


toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?

# Iterating over the contents of a Dictionary. for example
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, ext in cool_beasts.items():
    print("{} have {}".format(animal,ext))

# create count letter function
def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] +=1
    return result
print(count_letter("this is a long string"))

# In Python, a dictionary can only hold a single value for a given key. 
# To workaround this, our single value can be a list containing multiple values.
# Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
# Fill in the blanks to print a line for each item of clothing with each color, 
# for example: "red shirt", "blue shirt", and so on.
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for keys, values in wardrobe.items():
	for color in values:
		print("{} {}".format(color, keys))

# Complete the code to iterate through the keys and values of the car_prices dictionary
# printing out some information about each one.
def car_listing(car_prices):
  result = ""
  for modern,price in car_prices.items():
    result += "{} costs {} dollars".format(modern,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Taylor and Rory are hosting a party. They sent out invitations, 
# and each one collected responses into dictionaries, with names of their friends 
# and how many guests each friend is bringing. 
# Each dictionary is a partial list, but Rory's list has more current information about the number of guests. 
# Fill in the blanks to combine both dictionaries into one, with each friend listed only once, 
# and the number of guests from Rory's dictionary taking precedence, 
# if a name is included in both dictionaries. Then print the resulting dictionary.
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  guestTotal = guests2.copy()
  guestTotal.update(guests1)
  return guestTotal
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Use a dictionary to count the frequency of letters in the input string. 
# Only letters should be counted, not blank spaces, numbers, or punctuation.
# Upper case should be considered the same as lower case. For example, 
# count_letters("This is a sentence.") 
# should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    letters = letter.lower()
    #if letters not in text and letters != " ":
    if letters.isalpha():
        if letters not in result:
            result[letters] = 0
        # Add or increment the value in the dictionary
        result[letters] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}