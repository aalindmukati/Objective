from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
color=['red','blue','green','purple','black','orange']
screen.setup(500,400)
user_bet =screen.textinput('make ur bet', 'which object will win the race  red, blue, green, purple, black or orange')
print(user_bet)
y = [10,40,70,100,130,160]
all_racers = []


for turtle_thing in range(0,6):
    Aj = Turtle('turtle')
    Aj.color(color[turtle_thing])
    Aj.penup()
    Aj.goto(-235,y=y[turtle_thing])
    all_racers.append(Aj)

if user_bet:
    is_race_on=True

while is_race_on:

    for racers in all_racers:
        if racers.xcor() > 225:
            break
        randi_dist = random.randint(0,10)
        racers.forward(randi_dist)
    

print("Dekh le kaun jita aur fir khush hona h to hoja warna ja ")
screen.exitonclick()

