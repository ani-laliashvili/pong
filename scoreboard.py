from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 200)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def l_score_up(self):
        self.l_score += 1

    def r_score_up(self):
        self.r_score += 1

    def refresh(self):
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", move=False, align=ALIGNMENT, font=FONT)