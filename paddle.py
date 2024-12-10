from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(0, -170)
        self.shape("square")
        self.color("white")

    def move_right(self):
        self.forward(20)

    def move_left(self):
        self.backward(20)