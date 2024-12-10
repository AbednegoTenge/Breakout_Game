from turtle import *
import random
from bricks import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

speed = 2
brick = Brick()
ball = Ball()
scoreboard = Scoreboard()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


ts = []
rows = 5
columns = 13
x_spacing = 45
y_spacing = 25

for row in range(rows):
    for col in range(columns):
        x = -270.5 + col * x_spacing
        y = 250 - row * y_spacing
        t2 = brick.create_brick(x, y, colour=random.choice(colors))
        ts.append(t2)


paddle = Paddle()

screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")
screen.listen()


def breakout():
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.bounce_x()

    if ball.ycor() > 290:
        ball.bounce_y()
    if (
            paddle.xcor() - 40 <= ball.xcor() <= paddle.xcor() + 40
            and paddle.ycor() + 10 >= ball.ycor() >= paddle.ycor() - 10
    ):
        ball.bounce_y()

    if ball.ycor() < -190:
        scoreboard.game_over()
        return False

    for i in ts:
        if ball.distance(i) < 20:
            colour = i.fillcolor()
            i.hideturtle()
            ts.remove(i)
            ball.bounce_y()
            scoreboard.add_score(colour)

        scoreboard.increase_level(ts, speed)

    screen.ontimer(breakout, 20)

breakout()
screen.mainloop()