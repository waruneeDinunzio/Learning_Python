# Sorting List of Tuples
# take advantage of the ability to sort a list of tuples to get a sort version of dictionary
# 1. sort the dictionary by the key using the items() and sorted()
d = {'a':10, 'b' : 1, 'c' : 22}
print(d.items())
print(sorted(d.items()))  # sorted by key
t = sorted(d.items())
for k,v in sorted(d.items()):
    print(k,v)

# Sort by values instead of key
# if we could construct a list of tuples of the form (value, key) we could sort by value
# We do this with a for loop that create a list of tuples
c = {'a':10, 'b' : 1, 'c' : 22}
tmp = list()
for k, v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)  # reverse= higher value first
print(tmp)

# This is program to count top 10 most common words in file
fhand = open('list.py')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # idiom for making a histogram
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
    print(key, val)

# shorter version
print(sorted([ (v,k) for k,v in c.items() ]))  # called List comprehension
# List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it
