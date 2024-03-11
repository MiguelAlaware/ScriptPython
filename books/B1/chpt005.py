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

def estimate_pi():
    k = 0 
    sum = 0 
    third = 2 * math.sqrt(2) / 9801 
    while True:
        first = math.factorial(4 * k) * (1103 + 26390 * k) 
        second = math.factorial(k)**4 * 396**(4*k) 
        fourth = third * first / second 
        sum+=fourth 
        
        if abs(fourth) < 1e-15:
            break     

    
        k+=1  
    return 1 / sum

print(estimate_pi())
