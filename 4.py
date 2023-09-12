import turtle
import tkinter
import random

_ = 300
__ = 300
___ = 3
____ = 0

_____,______,_______,________,_________,__________,___________= [0] * 7

turtle.title('거북이 맘대로 싸돌아다니기')

turtle.shape('turtle')
turtle.pensize(___)
turtle.setup(width= __ + 30, height= __+30)
turtle.screensize(_,__)


while True :
    _____ = random.random()
    ______ = random.random()
    _______ = random.random()
    turtle.pencolor((_____,______,_______))


    ________ = random.randrange(0,360)
    _________ = random.randrange(1,100)
    turtle.left(h)
    turtle.forward(i)
    __________ = turtle.xcor()
    ___________ = turtle.ycor()

    if (-_ / 2 <= __________ and __________ <= _/2) and (-__/ 2 <= ___________ and ___________ <=__/ 2):
        pass
    else :
        turtle.penup
        turtle.goto(0,0)
        turtle.pendown

        ____ += 1 
        if ____ >= 5 :
            break 

turtle.done()