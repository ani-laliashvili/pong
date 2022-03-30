from turtle import Turtle

class ScreenDivider(Turtle):
    def __init__(self):
        super().__init__()
        self.position_divider()


    def position_divider(self):
        self.goto(0, -300)
        self.pendown()
        self.hideturtle()
        self.color('white')
        self.pensize(3)
        self.draw()


    def draw(self):
        self.setheading(90)
        for i in range(0, 30):
            if i % 2 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(20)