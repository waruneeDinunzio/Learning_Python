astr = 'Hello Bob'
try:
    istr = int(astr)  # this not gonna run
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

word = 'Bob'
try:
    print("hello")
    istr = int(word)  # this is an error so it'll jump to except:
    print('There')
except:
    word = -1
(print('Done', word))

# real world example
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a Number')

temp = "5 degrees"
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
