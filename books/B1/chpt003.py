import time

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

def print_n(s, n):
    if n <=0:
       return 
    print(s)
    print_n(s, n-1)




x = int(input("Give a value for x: "))

if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
elif x < 0:
    pass


