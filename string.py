word = 'bananana'
i = word.find("na")
print(i)  # 2 the index number of position if not find will return -1

# Slicing Strings
s = "Monty Python"
print(s[0:4])  # first 4 index

# String Concatenation
# using + same syntex as JavaScrip
print('Hello ' + s)

# split() made a list of string. split look for space to split.
abc = 'With three words'
stuff = abc.split()
print(stuff)
# more example
line = 'His e-mail is q-lar@freecodecamp.org'
pieces = line.split()  # split by emtry space
parts = pieces[3].split('-')  # split at '-'
print(parts[1])
counts = {'quincy':1, 'mrugest': 42, 'beau' : 100}
print(counts.get('kris', 0))
print(counts)


# Parsing and Extracting: this is an example
data = 'From warunee.dinunzio@umass.edu.usa Sat Jan 5 09:14:16 2021'
beginpos = data.find('@')
endpos = data.find(' ',beginpos)  #looking for space ' '
host = data[beginpos+1 : endpos]
print(host)

# NOTE in python 3, all string are Unicode (take foreige languge or non-latin charactor as String type)

# Reading files
# fhand = open('app.py')
# for line in fhand:
#     line = line.rsplit()  # to avoid white space
#     if line.startswith('print'):
#         print(line)
# # Skipping with continue
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rsplit()
#     if not line.startswith('From:'):
#         continue
#     print(line)

# Using in to select lines
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rsplit()
#     if not '@uct.ac.za' in line :
#         continue
#     print(line)

# Prompt for file name input
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count += 1
print('There were', count, 'subject lines in' , fname)

