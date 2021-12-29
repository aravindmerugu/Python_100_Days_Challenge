import random
from turtle import Turtle, Screen

colors = ["violet","indigo","blue","green","yellow","orange","red"]
racers = ["t1","t2","t3","t4","t5","t6","t7"]
screen = Screen()
screen.setup(width=500, height=400)
y_c = 120
for color in colors:
    racers[colors.index(color)] = Turtle(shape="turtle")
    racers[colors.index(color)].color(colors[colors.index(color)])
    racers[colors.index(color)].penup()
    racers[colors.index(color)].goto(x=-230,y=y_c)
    y_c-=30
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? enter a color")

if user_bet:
    is_game_on = True

while is_game_on:
    for racer in racers:
        if racer.xcor() > 230:
            is_game_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"you have won! the {winning_color} turtle is the winner!")
            else:
                print(f"you have lost! the {winning_color} turtle is the winner!")
        racer.forward(random.randint(1,10))
screen.exitonclick()