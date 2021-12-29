import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("orange")
colormode(255)
direction = [0, 90, 180, 270]

colors = ["Red",
          "Pink",
          "Orange",
          "Yellow",
          "Purple",
          "Green",
          "Blue",
          "Brown"]

timmy.speed("fastest")
for _ in range(72):
    timmy.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    timmy.circle(100)
    timmy.left(5)


screen.exitonclick()
