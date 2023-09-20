import turtle
import tkinter

t = turtle

t.shape("turtle")

t.penup()


while True :
    x  = int(input("좌표:"))
    y  = int(input("좌표:"))
    text=  input("글자:")
    
    t.goto(x,y)
    t.write(text, font=("맑은고딕",30))

t.done()
t.exitonclick()