from turtle import Turtle,Screen
import random

Aj = Turtle()
screen = Screen()
 
def forward():
    Aj.forward(20)


screen.listen()
screen.onkey(key ="space" , fun=forward)

screen.exitonclick()