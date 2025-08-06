from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.penup()
        self.dx = 10
        self.dy = 10
        self.changing_speed=0.1

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy*=-1

    def bounce_x(self):
        self.dx*=-1
        self.changing_speed*=0.9

    def reset_position(self):
        self.goto(0, 0)
        self.changing_speed=0.1
