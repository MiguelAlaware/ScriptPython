import turtle
import math


bob = turtle.Turtle()

print(bob)

def square(t, length):
    for i in range(4):
     t.fd(length)
     t.lt(90)
    


def polygon(t, length, n):
    angle = 360 / n 
    for i in range(n):
     t.fd(length)
     t.lt(angle)

    
def circle(t, r):
    polygon(t, r, 60)

def circle_remade(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1 
    length = circumference / n 
    polygon(t, length, n)



def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle  = angle / n 
    for i in range(n):
        t.fd(step_length) 
        t.lt(step_angle)

def petal(t, r, angle):
    for i in range(2): 
      arc(t, r, angle)
      t.lt(180-angle)
        
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


turtle.mainloop()



