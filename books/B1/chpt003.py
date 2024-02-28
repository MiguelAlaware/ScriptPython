import time
import turtle

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

def format_time(total_seconds):
    total_seconds = time.time() 
    hours = total_seconds // 3600
    days = hours // 24 
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    print(f"Days:{days}, Hours:{hours}, Minutes:{minutes}, Seconds:{seconds}")

def check_fermat():
    a = int(input("Value for [a]: "))
    b = int(input("Value for [b]: "))
    c = int(input("Value for [c]: "))
    n = int(input("Value for [n]: ")) 
    
    if n > 2:
        if a**n + b**n == c**n:
            print("Holy smokes,Fermat was wrong!")
        else:
            print("No that doesn't work")
        
def is_triangle(x, y, z):
    if x + y < z or x + z < y or y + z < x:
       print("No")
    else:
        print("Yes")

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1) 
    t.rt(2*angle) 
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)



x = int(input("Give a value for x: "))

if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
elif x < 0:
    pass


