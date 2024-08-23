import time
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        y_cor = random.randint(-250, 250)
        new_car = self.shape('square')
        new_car = self.color(COLORS[random.randint(0,5)])
        new_car = self.penup()
        new_car = self.shapesize(1, 2)
        new_car = self.goto(280, y_cor)
        new_car = self.left(180)


    def moveCar(self):
        self.forward(MOVE_INCREMENT)

