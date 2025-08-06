from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(270)
        self.lines()
        self.score_1=0
        self.score_2=0

    def lines(self):
        self.goto(0, 290)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def update_score(self):
        self.clear()
        self.lines()
        self.goto(-50,250)
        self.write(f"{self.score_1}", False, font=("Arial", 30, "normal"))
        self.goto(30,250)
        self.write(f"{self.score_2}", False, font=("Arial", 30, "normal"))

    def score1(self):
        self.score_1+=1
        self.update_score()

    def score2(self):
        self.score_2+=1
        self.update_score()