# Keeps track of score and high score, then displays it to the user
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    # Show high score and current score
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("High Score.txt", mode="r") as data:  # store high score in High Score.txt
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    # refresh scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # reset high score when the current score is higher than high score
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High Score.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # increase the score when food is eaten
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
