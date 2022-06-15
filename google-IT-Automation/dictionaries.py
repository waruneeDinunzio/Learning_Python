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
