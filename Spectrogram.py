from turtle import Turtle,Screen
import random

Aj = Turtle()
screen = Screen()

screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

angle = [0,30,45,60,90,120,270,180]

screen.screensize(100,100)
Aj.speed(20)

for path in range(45):
    Aj.color(random_color())
    Aj.circle(30)
    Aj.left(10)

Aj.goto(100,20)
Aj.goto(-100,20)
Aj.goto(0,0)
Aj.goto(100,-20)
Aj.goto(-100,-20)
Aj.goto(0,0)

screen.exitonclick()