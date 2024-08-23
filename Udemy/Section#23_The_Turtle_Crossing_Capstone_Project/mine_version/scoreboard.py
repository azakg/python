from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.lives = 4
        self.updateLevel()
        self.updateLives()

    def updateLevel(self):
        self.clear()
        self.goto(-100, 250)
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def updateLives(self):
        self.clear()
        self.goto(100, 250)
        self.lives -= 1
        self.write(f"Lives: {self.lives}", align="center", font=FONT)
