from turtle import Turtle

DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = DISTANCE
        self.y_move = DISTANCE
        self.speed = 1
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)

    def in_motion(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.speed = 1
        self.x_bounce()