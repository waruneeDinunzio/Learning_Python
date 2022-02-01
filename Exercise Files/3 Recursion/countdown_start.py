# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        print("Done")
    else:
        print(x)
        countdown(x-1)
        print("foo")



countdown(5)
