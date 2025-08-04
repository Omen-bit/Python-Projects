from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.setup(600,600)
screen.title("My snake Game")
screen.bgcolor("black")
screen.tracer(0)

sk=Snake()
food=Food()
score=ScoreBoard()

head = sk.container[0]
heading = head.heading()

screen.listen()
screen.onkey(sk.move_up,"Up")
screen.onkey(sk.move_down,"Down")
screen.onkey(sk.move_left,"Left")
screen.onkey(sk.move_right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.08)
    sk.move()

    if sk.container[0].distance(food) < 10:
        sk.extend()
        food.refresh()
        score.increase_score()

    if (
            sk.container[0].xcor() > 280 or
            sk.container[0].xcor() < -295 or
            sk.container[0].ycor() > 280 or
            sk.container[0].ycor() < -280
    ):
        is_game_on=False
        score.game_over()

    for elements in sk.container[1:]:
        if head.distance(elements) < 5:
            is_game_on = False
            score.game_over()




screen.exitonclick()