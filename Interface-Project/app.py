import turtle

def square(turtle, length):
    for i in range(4):
        turtle.fd(length)
        turtle.lt(90)
def polygon(turtle, length, n):
    for i in range(n):
        turtle.fd(length)
        turtle.lt(360 / n)
def circle(turtle, raio):
    turtle.circle(raio)

    

bob = turtle.Turtle()
circle(bob, 120)
turtle.mainloop()
