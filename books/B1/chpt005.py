import math

def print_n(s, n):
    while n > 0:
        print(s)
        n-=1

def mysqrt(a):
    x = a - 1
    while True:
        y = (x + a) / 2
        if y == x:
           return y 
        x = y
    
def test_sqrt(q):
    print("a   " + "mysqrt(a) " + "math.sqrt(a)") 
    print("- - - - - - - "  + "- "*len("math.sqrt(a)") ) 
    n = 1 
    while n < q:
     x = mysqrt(n) 
     y = math.sqrt(n) 
     print(f"{n}   {x}       {y}") 
     n += 1

def eval_loop():
    while True:
        line = str(input("> "))
        if line.lower() == "done":
            break
        print(f">> {eval(line)}")


def estimate_pi(k):
    while k > 1e-15:
    



    
