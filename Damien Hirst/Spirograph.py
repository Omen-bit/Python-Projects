import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
timmy=Turtle()
timmy.shape("turtle")
timmy.color("green")

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    return r,g,b

rotation=360//5

for _ in range(rotation):
    timmy.right(5)
    timmy.pencolor(random_colour())
    timmy.circle(80)
    timmy.speed(0)


screen=Screen()
screen.exitonclick()