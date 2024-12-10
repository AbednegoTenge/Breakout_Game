from turtle import Turtle
from tkinter import messagebox, Tk


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.highest_score = self.read_highest_score()
        self.level = 1
        self.speed(5)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Current_Score:{self.score}", align="center", font=("Courier", 12, "normal"))
        self.goto(-250, 270)
        self.write(f"Highest_Score:{self.highest_score}", align="left", font=("Courier", 12, "normal"))

    def add_score(self, colors):
        if colors == "green":
            self.score += 3
        elif colors == "orange":
            self.score += 5
        elif colors == "red":
            self.score += 9
        else:
            self.score += 1
        self.update_scoreboard()

    def game_over(self):
        tk = Tk()
        tk.withdraw()
        messagebox.showerror(message="Game Over!")
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.save_score()
        self.update_scoreboard()

    @staticmethod
    def read_highest_score():
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.highest_score))

    def increase_level(self, ts, speed):
        if not ts:
            self.level += 1
            speed += 2
            self.speed(speed)