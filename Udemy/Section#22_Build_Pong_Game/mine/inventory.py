from turtle import Turtle
import random



class Inventory:
    def __init__(self):
        self.b_segment = []
        self.ball()
        self.grid()

    def ball(self):
        new_ball = Turtle(shape="circle")
        new_ball.penup()
        new_ball.color("white")
        new_ball.goto(0, random.randint(-200, 200))
        self.b_segment.append(new_ball)

    def grid(self):
        for y in range(-290, 290, 30):
            for i in range(3):
                y += 5
                new_grid = Turtle(shape="square")
                new_grid.shapesize(0.5)
                new_grid.color("white")
                new_grid.penup()
                new_grid.goto(0, y)



    def ballMovement(self):
        self.b_segment[0].speed('slow')
        self.b_segment[0].forward(10)

