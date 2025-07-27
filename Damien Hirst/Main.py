import random
import turtle
from turtle import Turtle,Screen
# import colorgram

# colour=colorgram.extract('spot painting .jpg',30)
# container=[]

timmy=Turtle()
turtle.colormode(255)
timmy.color("green")
timmy.shape("turtle")

# for color in colour:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     container.append((r,g,b))
#
# print(container)

rgb_list=[(237, 243, 250), (235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68), (230, 52, 128), (196, 77, 19), (217, 133, 177), (193, 164, 15), (34, 106, 166), (11, 21, 62), (32, 189, 114), (232, 224, 4), (18, 28, 171), (122, 188, 161), (204, 32, 127), (233, 165, 197), (14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10), (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218, 232), (229, 73, 45), (169, 180, 229)]
timmy.teleport(-150,-150)
y_axis=-150
for _ in range(10):
    for _ in range(10):
        timmy.pencolor(random.choice(rgb_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    y_axis+=40
    timmy.teleport(-150, y_axis)



screen=Screen()
screen.exitonclick()