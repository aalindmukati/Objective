from turtle import Turtle,Screen
import random

Aj = Turtle()
screen = Screen()

colors = ['red','blue','green','cyan','black',]
size = [0,30,45,60,90,120,270,180]

screen.screensize(100,100)
Aj.speed(30)

for path in range(25):
    Aj.color(random.choice(colors))
    Aj.circle(15)
    Aj.left(15)


screen.exitonclick()