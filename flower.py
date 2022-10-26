import turtle


turtle.bgcolor("#141E27")
line = turtle.Turtle()
line.speed(100)
line.pencolor("#FDEFF4")

for i in range(300):
    line.circle(190-i, 90)
    line.left(90)
    line.circle(190-i, 90)
    line.left(10)
    

turtle.done()   