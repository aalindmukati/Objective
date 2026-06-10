from turtle import Turtle,Screen

Aj = Turtle()
screen = Screen()
screen.setup(600,600)
screen.bgcolor('purple')

starting_pos = [ (0,0),(-20,0),(-40,0)]

for position in starting_pos:
    segment = Turtle("square")
    segment.goto(starting_pos)


screen.exitonclick()