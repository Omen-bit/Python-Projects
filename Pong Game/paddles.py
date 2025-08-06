from turtle import Turtle,Screen

screen=Screen()
screen.listen()

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.state(position)

    def state(self,position):
        self.goto(position)

    def move_up(self):
        if self.ycor()>240:
            y=self.ycor()
            self.goto(self.xcor(), y)

        else:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def move_down(self):
        if self.ycor() < -230:
            y = self.ycor()
            self.goto(self.xcor(), y)
        else:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)





