from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        self.update_score()

    def update_score(self):
        self.write(f"Score= {self.score}",False,"center",("Arial",15,"normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over",False,"center",("Arial",15,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
