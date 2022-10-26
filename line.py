import turtle
from turtle import *

scrn = turtle.Screen()
line = turtle.Turtle()

line.speed(1000)

scrn.bgcolor("#F8EDE3")

for i in range(180):
    line.forward(100)
    line.right(30)
    line.forward(20)
    line.left(60)
    line.forward(50)
    line.right(30)
    

    line.penup()
    line.setposition(0, 0)
    line.pendown()

    line.right(2)

turtle.done()