from turtle import Screen
from screen_divider import ScreenDivider
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.bgcolor('black')
screen.setup(WIDTH, HEIGHT)
screen.title("Pong")
screen.tracer(0)
screen_divider = ScreenDivider()

r_paddle = Paddle(-370)
l_paddle = Paddle(370)

# set key responses
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1/ball.speed)
    screen.update()
    ball.in_motion()

    # detects collision with upper/lower walls
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.y_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() > 340 or ball.distance(r_paddle) < 50 and ball.xcor() < -340:
        ball.speed += 0.1
        ball.x_bounce()
    elif ball.xcor() > 380:
        print("Right Player Loses")
        scoreboard.l_score_up()
        scoreboard.refresh()
        ball.reset_position()
    elif ball.xcor() < -380:
        print("Left Player Loses")
        scoreboard.r_score_up()
        scoreboard.refresh()
        ball.reset_position()

screen.exitonclick()


