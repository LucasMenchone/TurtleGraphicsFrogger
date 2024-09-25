FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260, 240)
        self.write("SCORE 0", False, align="left", font=FONT)

    def score_update(self, points):
        self.clear()
        self.write("SCORE " + str(points), False, align="left", font=FONT)

    @staticmethod
    def game_over_screen():
        go = Turtle()
        go.hideturtle()
        go.write("GAME OVER", move=False, align="center", font=FONT)

