import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_game = True

def play_game():
    is_game_on = True
    global is_game
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_scoreboard()
            snake.extend()

        #detect collision with wall
        if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
            scoreboard.game_over()
            is_game_on = False
            is_game = False

        #detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                is_game_on = False
                is_game = False

play_game()
if is_game == False and screen.onkey(play_game(),"space"):
    is_game = True
    play_game()
screen.exitonclick()
