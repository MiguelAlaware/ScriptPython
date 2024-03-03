import math
import re

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

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n - 1) + fibonacci(n - 2)

def new_factorial(n):
    if not isinstance(n, int):
       print("Factorial is only defined for integers")
       return None
    elif n < 0:
        print("Factorial is not defined for negative integers")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def ack(m, n):
    if m == 0:
       return n+1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
       return ack(m - 1, ack(m, n-1))
    
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palyndrome(word):
    if len(word) > 2: 
       palyndrome = last(word)+ middle(word) +first(word)
       if word == palyndrome:
          return True
       else:
          return False

def is_power(a, b):
    if a > 0 and b > 0:
        if a % b == 0 or b % b/a == 0:
            return True
        else:
            return False

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)



