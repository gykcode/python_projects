import turtle


turtle.bgcolor("#141E27")
line = turtle.Turtle()
line.speed(100)
line.pencolor("#CC9544")

for i in range(400):
    line.forward(i)
    line.left(92)

turtle.done()   
