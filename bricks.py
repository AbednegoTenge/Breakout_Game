from turtle import Turtle


class Brick:

    def __init__(self):
        self.bricks = []

    @staticmethod
    def create_brick(a, b, colour):
        t2 = Turtle()
        t2.shape("square")
        t2.shapesize(stretch_wid=1, stretch_len=2)
        t2.penup()
        t2.color(colour)
        t2.goto(a, b)
        return t2
