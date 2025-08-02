from turtle import Turtle,Screen
from tkinter import messagebox
import random

screen=Screen()
screen.setup(600,500)

colour = ["green", "yellow", "blue", "magenta", "red", "orange"]

while True:
    choice = screen.textinput("Make a Guess", "Select the colour of the turtle you want to bet : ").lower()
    is_game_on=False
    if choice in colour:
        is_game_on=True
        break
    else:
        messagebox.showinfo("Invalid colour sequence","Choose a colour from (green,yellow,blue,purple,red,orange)")

all_turtles=[]

y=200
for index in range(6):
    new_turtle=Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colour[index])
    y=y-50
    new_turtle.goto(-250, y)
    all_turtles.append(new_turtle)
    
while is_game_on:
    for values in all_turtles:
        values.forward(random.randint(1, 10))
        if values.xcor() > 268:
            is_game_on=False
            winning_colour=values.pencolor()
            break

if winning_colour==choice:
    messagebox.showinfo("You Win",f"{winning_colour} is the winner")
else:
    messagebox.showinfo("You loose",f"{winning_colour} is the winner")
screen.bye()
