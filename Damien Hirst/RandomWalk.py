import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
timmy=Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.pensize(10)

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    return r,g,b

for _ in range(200):
    timmy.pencolor(random_colour())
    timmy.forward(40)
    timmy.setheading(random.choice([90,180,270,360]))

screen=Screen()
screen.exitonclick()
