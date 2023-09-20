import turtle
import tkinter
import random
from tkinter.simpledialog import*

t = turtle

instr = ''

sso, sinso = 300,300

cc,dd,ee=[0]*3

t.title("하이요")
t.shape('turtle')
t.setup(width= sso + 50 , height= sinso +50)
t.screensize(sso,sinso)
turtle.penup()

instr = askstring('문자열 입력','거북이가 쓸 문자열을 입력')

for ch in instr :
    cc = random.randrange(-sso / 2,sso /2)
    dd = random.randrange(-sinso / 2,sinso / 2)
    r = random.random()
    g = random.random()
    b = random.random()
    ee = random.randrange(10,50)

    t.goto(cc,dd)
    t.pencolor((r,g,b))
    t.write(ch,font=('맑은고딕',ee,'bold'))


t.exitonclick()
