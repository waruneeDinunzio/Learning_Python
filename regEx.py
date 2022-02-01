import re
# using re.search() like startswith() returns a True/False depending on whether the string matches
# Matching and Extracting Data using re.findall() to match strings to be extracted.
x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('AEIOU+',x)
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
a = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

# String Parsing Examples
data = "From stephem.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
# The Double split pattern
words = data.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[0])
y = re.findall('@([^ ]*)',data)
print(y)
# Escape Character \
x = 'we just received $10.00 for cookies.'
z = re.findall('\$[0-9.]+',x)
print(z)


