from turtle import Turtle,Screen

t = Turtle()
print(t)

my_screen = Screen()
print(my_screen.canvheight)
t.color("Black")
t.speed(0.5)
t.forward(200)
t.right(45)
t.forward(150)
t.right(135)
t.forward(410)
t.right(135)
t.forward(150)
my_screen.bgcolor("Purple")

my_screen.exitonclick()