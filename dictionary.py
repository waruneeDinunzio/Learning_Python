counts = dict()  # create emtpy dictionary
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)
# get method use to check to see if a key is alraady in a dictionary and assuming a default value
for name in names:
    counts[name] = counts.get(name, 0) +1
print(counts)

# example using with loop
count = {'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in count:
    print(key, count[key])

# Retrieving lists of keys and values. you can get a list of Keys, values or items(both) from a dictionary
jjj = {'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(list(jjj))
print(jjj.values())
print(jjj.items())  # tuple?

# Two Iteration variables! : we loop through the key-value pair in a dict using 2 iteration var
# first variable is the key and second variable is value of the key
for aaa,bbb in jjj.items():
    print(aaa,bbb)

# other example
name = input('Enter file: ')
handle = open(name)
countWords = dict()
for line in handle:
    words = line.split()
    for word in words:
        countWords[word] = countWords.get(word,0) + 1
bigcount = None
bigword = None
for word,count in countWords.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


