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
Aj.speed(30)

for path in range(50):
    Aj.color(random_color())
    Aj.circle(30)
    Aj.left(random.choice(angle))


screen.exitonclick()