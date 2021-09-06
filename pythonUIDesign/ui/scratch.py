import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
turtle.pencolor("magenta")


def drawCircle(radius):
    for i in range(5):
        turtle.circle(radius)
        radius -= 10


def drawDesign():
    for i in range(10):
        drawCircle(150)
        turtle.right(36)


drawDesign()
turtle.exitonclick()
