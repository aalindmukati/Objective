from turtle import Turtle,Screen
import random

Aj = Turtle()
screen = Screen()
 
def forward():
    Aj.forward(20)
def left():
    Aj.left(90)
def right():
    Aj.right(90)

screen.listen()
screen.onkey(key ="space" , fun=forward)
screen.onkey(key="d", fun=left)
screen.onkey(key="a", fun=right)


screen.exitonclick()