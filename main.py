from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.detect_wall():
        ball.bounce_y()

    if ball.detect_paddle(r_paddle) or ball.detect_paddle(l_paddle):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()
        scoreboard.update()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()
        scoreboard.update()


screen.exitonclick()
