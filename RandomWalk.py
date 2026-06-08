from turtle import Turtle,Screen
import random

Aj = Turtle()
screen = Screen()

colors = ['red','blue','green','yellow','black']
direction = [0,60,90,270,180]

for path in range(1,51):
    Aj.forward(36)
    Aj.setheading(random.choice(direction))

screen.exitonclick()