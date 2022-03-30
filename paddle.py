from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xpos):
        super().__init__()
        self.draw(xpos)


    def draw(self, xpos):
        self.goto(xpos, 0)
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)