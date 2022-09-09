from turtle import Turtle, Screen
from pong import Pong
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
l_paddle = Pong((-370, 0))
r_paddle = Pong((370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "e")
screen.onkey(r_paddle.go_down, "d")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collison with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle

    if r_paddle.distance(ball) < 40 and ball.xcor() > 340 or l_paddle.distance(ball) < 40 and ball.xcor() < -340:
        ball.bounce_x()

    #detect right paddle misses

    if ball.xcor() > 380:
        scoreboard.r_score()
        ball.reset_position()

    # detect left paddle misses

    if ball.xcor() < -380:
        scoreboard.l_score()
        ball.reset_position()



screen.exitonclick()
