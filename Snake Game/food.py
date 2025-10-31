<<<<<<< HEAD
from turtle import Turtle
import random


def position():
    return random.randint(-280,280)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        self.goto(position(),position())
=======
from turtle import Turtle
import random


def position():
    return random.randint(-280,280)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        self.goto(position(),position())
>>>>>>> 9e3580f51be5e229dc837d659b4a59ea05cded37
