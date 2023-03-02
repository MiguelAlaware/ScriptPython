import turtle, math

def square(t, length):
   t = turtle.Turtle()
   for i in range(4):
        t.fd(length)
        t.lt(90)
   turtle.mainloop()
   print(t)


def polygon(t, length, n):
    t = turtle.Turtle()
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop()
    print(t)

def circle(tu, r):
    polygon(tu, 10, r)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
        
arc(turtle, 100, 360*4)