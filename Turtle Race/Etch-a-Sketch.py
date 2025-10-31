<<<<<<< HEAD
from turtle import Turtle,Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("green")

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def counterClock():
    timmy.left(10)

def clock():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.home()
    timmy.clear()


screen=Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counterClock)
screen.onkey(key="d",fun=clock)
screen.onkey(key="c",fun=clear)
screen.exitonclick()

=======
from turtle import Turtle,Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("green")

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def counterClock():
    timmy.left(10)

def clock():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.home()
    timmy.clear()


screen=Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counterClock)
screen.onkey(key="d",fun=clock)
screen.onkey(key="c",fun=clear)
screen.exitonclick()

>>>>>>> 9e3580f51be5e229dc837d659b4a59ea05cded37
