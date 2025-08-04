from turtle import Turtle,Screen

POS=[(0,0),(-20,0),(-40,0)]

screen=Screen()
screen.listen()


class Snake:

    def __init__(self):
        self.container=[]
        self.create_snake()

    def create_snake(self):
        for body in POS:
            self.structure(body)

    def structure(self,body):
        snake = Turtle("square")
        snake.penup()
        snake.goto(body)
        snake.color("white")
        self.container.append(snake)

    def extend(self):
        self.structure(self.container[-1].position())

    def move_up(self):
        if self.container[0].heading()==0 or self.container[0].heading()==180:
            self.container[0].setheading(90)


    def move_left(self):
        if self.container[0].heading() == 90 or self.container[0].heading() == 270:
            self.container[0].setheading(180)

    def move_right(self):
        if self.container[0].heading() == 90 or self.container[0].heading() == 270:
            self.container[0].setheading(0)

    def move_down(self):
        if self.container[0].heading() == 0 or self.container[0].heading() == 180:
            self.container[0].setheading(270)

    def move(self):
        for elements in range(len(self.container) - 1, 0, -1):
            new_x = self.container[elements - 1].xcor()
            new_y = self.container[elements - 1].ycor()
            self.container[elements].goto(new_x, new_y)

        self.container[0].forward(10)
