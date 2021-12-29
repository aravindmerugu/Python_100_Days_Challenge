# import colorgram
# colors = colorgram.extract('spot_painting.jpg', 10)
#
# rgb = []
#
# for color in colors:
#     rgb.append((color.rgb.r,color.rgb.g, color.rgb.b))
import random
from turtle import Turtle, Screen, colormode

colormode(255)
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")

colors_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204),
               (224, 234, 230), (142, 178, 203), (139, 82, 105)]
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
dot_counts = 100
timmy.speed("fastest")
for dot in range(1, dot_counts+1):
    timmy.dot(20, random.choice(colors_list))
    timmy.forward(50)
    if dot % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()

