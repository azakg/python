import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(turtle.moveUP, "Up")
screen.onkey(turtle.moveBack, "Down")

game_is_on = True
cars_counter = 0
carsList = []
lives = 3
gameSpeed = 0.1


def carLauncher():
    global cars_counter
    if cars_counter == 6:
        car = CarManager()
        carsList.append(car)
    cars_counter += 1
    if cars_counter > 6:
        cars_counter = 0
    for i in carsList:
        i.moveCar()

def collision():
    global game_is_on
    global lives
    for i in carsList:
        if turtle.distance(i) < 40:
            turtle.reset()
            lives -= 1
        if lives == 0:
            game_is_on = False
            turtle.color("red")


while game_is_on:
    time.sleep(gameSpeed)
    screen.update()
    carLauncher()
    collision()
    if turtle.ycor() > 280:
        turtle.reset()
        scoreboard.updateLevel()
        gameSpeed *= 0.8





