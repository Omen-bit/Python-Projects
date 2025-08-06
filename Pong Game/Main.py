import time
from turtle import Screen
from paddles import Paddle
from scoreboard import Scoreboard
from pong import Pong

screen=Screen()
screen.title("Classic Pong Game")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

paddle1=Paddle((-387,0))
paddle2=Paddle((380,0))
part=Scoreboard()
pong=Pong()

screen.listen()
screen.onkeypress(paddle2.move_up,"Up")
screen.onkeypress(paddle2.move_down,"Down")

screen.onkeypress(paddle1.move_up,"w")
screen.onkeypress(paddle1.move_down,"s")

part.update_score()
part.update_score()
game_is_on=True
while game_is_on:
    time.sleep(pong.changing_speed)
    screen.update()
    pong.move()

    if pong.ycor()>280 or pong.ycor()<-270:
        pong.bounce_y()

    if (pong.xcor()>350 and pong.distance(paddle2)<50) or (pong.xcor()<-350 and pong.distance(paddle1)<50):
        pong.bounce_x()

    if pong.xcor()>410:
        part.score1()
        pong.reset_position()

    if pong.xcor()<-410:
        part.score2()
        pong.reset_position()



screen.exitonclick()

