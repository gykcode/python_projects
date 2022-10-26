import turtle

line = turtle.Turtle()
line.up()
line.goto(0, -100)  
line.down()

line.begin_fill()
line.fillcolor("yellow")  
line.circle(100)
line.end_fill()

line.up()
line.goto(-67, -40)
line.setheading(-60)
line.width(5)
line.down()
line.circle(80, 120)    
line.fillcolor("black")

for i in range(-35, 105, 70):
    line.up()
    line.goto(i, 35)
    line.setheading(0)
    line.down()
    line.begin_fill()
    line.circle(10)   
    line.end_fill()
    
turtle.done()