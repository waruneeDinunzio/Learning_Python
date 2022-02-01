weight = float(input("Weight: "))  # use float or int() to convert string
convert = input("(K) or (L)bs: ")
# input() alway return String and String is not number
if convert.upper() == "K":
    converted = weight/0.45
    print("Weight in Lbs: " + str(converted)) # can not concat string to number
else:
    converted = weight*0.45
    print("Weight in Kbs: " + str(converted))
