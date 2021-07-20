import turtle

forwardValue = 0
rightValue = 0

turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("blue")
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

while True:
    turtle.forward(forwardValue)
    turtle.right(rightValue)
    forwardValue += 3
    rightValue += 1
    if rightValue == 200:
        break
turtle.exitonclick()
