from curses import window
import turtle

draw = turtle.Turtle()

def curve():
    draw.pen(pencolor="white", pensize= 3, speed= 3)
    for i in range(200):
        draw.rt(1)
        draw.fd(1)

def heart():
    draw.pen(pencolor="#DD5353", fillcolor="#DD5353", pensize= 3, speed= 3)
    draw.shape("turtle")
    draw.shapesize(1, 1, 1)
    draw.begin_fill()
    draw.lt(50)
    draw.fd(113)
    curve()
    draw.lt(120)
    curve()
    draw.fd()
    draw.end_fill()

    draw.hideturtle()


window = turtle.Screen()
window.bgcolor("#3C4048")

draw.penup()
draw.goto(-80, 300)
draw.pendown()
draw.shapesize(1, 2, 1)

draw.pen(pencolor="#DBC8AC", fillcolor="#DBC8AC", speed= 3)
draw.begin_fill()

draw.circle(60)
draw.lt(90)
draw.penup()
draw.fd(20)
draw.pendown()
draw.rt(90)
draw.circle(40)
draw.rt(90)
draw.penup()
draw.fd(20)
draw.lt(90)

draw.end_fill()

draw.fd(100)
draw.circle(60, extent=60)
draw.pendown()

draw.pen(pencolor="#DBC8AC", fillcolor="#DBC8AC", pensize=3, speed=3)
draw.begin_fill()

draw.lt(30)

draw.fd(85)
draw.lt(90)
draw.fd(20)
draw.lt(90)
draw.fd(70)
draw.circle(-20, extent=180)
draw.fd(70)
draw.lt(90)

draw.fd(20)
draw.lt(90)
draw.fd(85)
draw.circle(40, extent=180)

draw.end_fill()

draw.penup()

draw.rt(180)
draw.fd(35)
draw.lt(90)
draw.fd(140)
draw.lt(90)
draw.pendown()

heart()

turtle.done()
