def double_word(word):
    words = word*2
    return words + str(len(words))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
name = "waruneeD"
lastIndex = name[len(name)-1]
lastNegativeIndexes = name[-1]
print(lastIndex)
print(lastNegativeIndexes)

# Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. 
# Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
def first_and_last(message):
    if (len(message)==0):
        return True
    firstLetter = message[0]
    lastLetter = message[-1]
    if (firstLetter == lastLetter ):
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# Slice
slice = name[0:2]
slice2 = name[:2]
slice3 = name[2:]
print(slice)
print(slice2)
print(slice3)

#Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case.
def initials(phrase):
    words = phrase.upper().split()
    result = ""
    for word in words:

        result += 
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS