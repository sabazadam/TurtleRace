from turtle import Turtle, Screen
from random import randint
screen = Screen()
x = -200
y = -140
screen.colormode(255)
turtleList = []
colorList = ["cyan", "AliceBlue","DeepSkyBlue","DarkGrey","brown","beige"]
for i in range(6):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x,y)
    turtle.shapesize(2)
    turtle.color(colorList[i])
    y += 70
    turtle.speed("slowest")
    turtleList.append(turtle)
while True:
    randomIndex = randint(0,5)
    turtleList[randomIndex].forward(10)
    if turtleList[randomIndex].pos()[0] >335:
        print(turtleList[randomIndex].color()[0])
        break

screen.exitonclick()