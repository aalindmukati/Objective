import random
import time
from turtle import Screen, Turtle

# --- Screen Setup ---
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("chartreuse4")
screen.title("Snake Game")
screen.tracer(0)

def snake_game():
    # --- Game State Variables ---
    starting_pos = [(0, 0), (-20, 0), (-40, 0)]
    snake = []
    score = 0

    # --- Create the Snake ---
    for position in starting_pos:
        segment = Turtle("square")
        segment.color("DarkBlue")
        segment.penup()
        segment.goto(position)
        snake.append(segment)

    def display_game_over(reason):
        game_over.write(f"GAME OVER\n{reason}", align="center", font=("Arial", 24, "bold"))

    

    # --- Game Over ---
    game_over = Turtle()
    game_over.hideturtle()
    game_over.color('white')
    game_over.penup()
    game_over.goto(0,0)

    # --- Create the Food ---
    food = Turtle("square")
    food.color("red")
    food.penup()
    food.shapesize(stretch_len=0.7, stretch_wid=0.7)  # Make food slightly smaller
    food.goto(
        random.randint(-280, 280), random.randint(-280, 280)
    )  # Initial random position


    # --- Movement Functions ---
    def go_up():
        if snake[0].heading() != 270:  # Prevent snake from reversing into itself
            snake[0].setheading(90)


    def go_down():
        if snake[0].heading() != 90:
            snake[0].setheading(270)


    def go_left():
        if snake[0].heading() != 0:
            snake[0].setheading(180)


    def go_right():
        if snake[0].heading() != 180:
            snake[0].setheading(0)


    # --- Keyboard Bindings ---
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")

    # --- Main Game Loop ---
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)  # Controls the speed of the game

        # Move the snake body: segments follow the one in front of them
        for seg_num in range(len(snake) - 1, 0, -1):
            new_x = snake[seg_num - 1].xcor()
            new_y = snake[seg_num - 1].ycor()
            snake[seg_num].goto(new_x, new_y)

        # Move the snake head forward
        snake[0].forward(20)

        # Detect collision with food
        if snake[0].distance(food) < 15:
            # Move food to a new random location
            food.goto(random.randint(-280, 280), random.randint(-280, 280))

            # Add a new segment to the snake
            new_segment = Turtle("square")
            new_segment.color("DarkBlue")
            new_segment.penup()
            # Position it at the current last segment's spot
            new_segment.goto(snake[-1].position())
            snake.append(new_segment)

        # Detect collision with walls
        if (
            snake[0].xcor() > 290
            or snake[0].xcor() < -290
            or snake[0].ycor() > 290
            or snake[0].ycor() < -290
        ):
            game_is_on = False
            display_game_over('HIT A WALL')
            screen.update()

        # Detect collision with own tail
        for segment in snake[1:]:  # Check all segments except the head
            if snake[0].distance(segment) < 10:
                game_is_on = False
                display_game_over("BIT UR OWN TAIL")
                screen.update()


while True:
    try :
        user_choice = int(input("press 1 to play the game or press 2 to not play obv bruh"))
        if user_choice == 1:
            snake_game()
        elif user_choice == 2:
            print("Thanks for playing!")
            screen.bye()  # Closes the window
            break
        else:
            print("Invalid option. Please choose 1 or 2.")
    except ValueError:
        print("Please enter a valid number.")



screen.exitonclick()
