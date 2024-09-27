FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode="r") as high_score_file:
            self.high_score = high_score_file.read()
        self.hideturtle()
        self.penup()
        self.goto(-260, 240)
        self.write("SCORE: 0 HIGH SCORE: " + self.high_score, False, align="left", font=FONT)

    def score_update(self, points):
        self.clear()
        if points > int(self.high_score):
            with open("high_score.txt", mode="r+") as high_score_file:
                high_score_file.write(str(points))
                self.write("SCORE " + str(points) + " HIGH SCORE: " + str(points), False, align="left", font=FONT)
        else:
            self.write("SCORE " + str(points) + " HIGH SCORE: " + self.high_score, False, align="left", font=FONT)

    @staticmethod
    def game_over_screen():
        go = Turtle()
        go.hideturtle()
        go.write("GAME OVER", move=False, align="center", font=FONT)

