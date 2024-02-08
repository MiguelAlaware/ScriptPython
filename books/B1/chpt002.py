import turtle

bob = turtle.Turtle()

print(bob)

def square(t, length):
    for i in range(4):
     t.fd(length)
     t.lt(90)
    


def polygon(t, length, n):
    angle = 360 / n 
    circumference = length * n 
    for i in range(n):
     t.fd(length)
     t.lt(angle)

    
def circle(t, r):
    polygon(t, r, 60)

circle(bob, 10)

turtle.mainloop()

