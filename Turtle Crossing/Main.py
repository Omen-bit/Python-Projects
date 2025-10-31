from turtle import Screen
from structure import Structure
from blocks import Blocks
import time

screen = Screen()
screen.setup(width=600, height=400)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Structure()

blocks = Blocks()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
speed = 0.1

while game_is_on:
    time.sleep(speed)
    screen.update()

    blocks.move_blocks()

    blocks.create_block()

    for car in blocks.all_blocks:
        if car.distance(player) < 25:
            player.game_over()
            game_is_on = False

    if player.ycor() > 180:
        player.reset_position()
        speed *= 0.9
        blocks.increase_speed()

screen.exitonclick()
