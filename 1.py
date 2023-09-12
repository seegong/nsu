import turtle 
import tkinter
import random


def screenLeftclick(x, y) :
    global r, g, b
    turtle.pencolor ((r, g, b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightclick(x, y) :
    turtle.penup()
    turtle.goto(x, y)

def screenMidclick(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()


turtle.exitonclick()