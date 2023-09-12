import turtle
import tkinter
import random

a = 300
_ = 300
c = 3
d = 0

r,g,b,h,i,j,e = [0] * 7

turtle.title('거북이 맘대로 싸돌아다니기')

turtle.shape('turtle')
turtle.pensize(c)
turtle.setup(width= a + 30, height= _+30)
turtle.screensize(a,_)


while True :
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))


    h = random.randrange(0,360)
    i = random.randrange(1,100)
    turtle.left(h)
    turtle.forward(i)
    j = turtle.xcor()
    e = turtle.ycor()

    if (-a / 2 <= j and j <= a/2) and (-_ / 2 <= e and e <=_ / 2):
        pass
    else :
        turtle.penup
        turtle.goto(0,0)
        turtle.pendown

        d += 1 
        if d >= 5 :
            break 

turtle.done()