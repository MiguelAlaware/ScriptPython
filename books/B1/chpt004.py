import math

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def hypotenuse(aside, bside):
    return math.sqrt(aside**2 + bside**2) 

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False






      
