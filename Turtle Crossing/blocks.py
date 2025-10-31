from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class Blocks:
    def __init__(self):
        self.all_blocks = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_block(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_block = Turtle("square")
            new_block.shapesize(stretch_wid=1, stretch_len=2)
            new_block.penup()
            new_block.color(random.choice(COLORS))
            random_y = random.randint(-150, 150)
            new_block.goto(300, random_y)
            self.all_blocks.append(new_block)

    def move_blocks(self):
        for block in self.all_blocks:
            block.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
