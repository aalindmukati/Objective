from turtle import Turtle,Screen
import random

Aj = Turtle()
screen = Screen()

colors = ['red','blue','green','cyan','black']
direction = [0,30,45,60,90,120,270,180]

screen.screensize(100,100)
Aj.speed(10)

for path in range(70):
    Aj.color(random.choice(colors))
    Aj.forward(30)
    Aj.setheading(random.choice(direction))

Aj.goto(0,0)

screen.exitonclick()