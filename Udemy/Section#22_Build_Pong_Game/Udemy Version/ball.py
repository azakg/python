from turtle import Turtle
import random

x_variable = 10
y_variable = 10

signs = [10, -10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()


    def move(self):

        new_x = self.xcor()
        new_y = self.ycor()

        if new_y == 280:
            new_y = self.ycor() - y_variable
            signs[1] = -10
        elif new_y == -280:
            new_y = self.ycor() + y_variable
            signs[1] = 10
        elif new_x == 380:
            new_x = self.xcor() - x_variable
            signs[0] = -10
        elif new_x == -380:
            new_x = self.xcor() + x_variable
            signs[0] = 10
        else:
            new_x = self.xcor() + signs[0]
            new_y = self.ycor() + signs[1]

        self.goto(new_x, new_y)



