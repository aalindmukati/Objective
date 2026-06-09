from turtle import Turtle,Screen
import random


screen = Screen()
color=['red','blue','green','purple','black','orange']
screen.setup(500,400)
user_bet =screen.textinput('make ur bet', 'which object will win the race  red, blue, green, purple, black or orange')
print(user_bet)
y = [10,40,70,100,120]

for turtle_thing in range(0,6):
    Aj = Turtle('turtle')
    Aj.color(color[turtle_thing])
    Aj.penup()
    Aj.goto(-235,y=y[turtle_thing])




screen.exitonclick()
