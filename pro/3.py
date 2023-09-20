import turtle
import tkinter


turtle.shape("turtle")          
turtle.pensize(5) # 펜의 두께: 5
turtle.pencolor("blue") # 펜의 색상: 파란색

while True :
    angle = int(input("거북이의 회전 각도 : "))
    distance = int(input("거북이의 이동 거리 : "))
    turtle.right(angle)
    turtle.forward(distance)


turtle.exitonclick()