from turtle import Turtle,Screen

jason = Turtle()
my_screen = Screen()

jason.shape("turtle")
jason.color('green')
my_screen.bgcolor('orange')

jason.speed(3)
jason.goto(100,15)
jason.goto(212,190)
jason.goto(-122,122)
jason.goto(0,0)

my_screen.exitonclick()