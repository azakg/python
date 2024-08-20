from turtle import Turtle, Screen
from gamers import GamerRight, GamerLeft
from inventory import Inventory
import time


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

gamerR = GamerRight()
gamerL = GamerLeft()
ball = Inventory()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.ballMovement()

    def follow_mouse():
        x, y = screen.cv.winfo_pointerxy()
        gamerR.goto(0, screen.window_height() // 2 - y)
        screen.ontimer(follow_mouse, 10)

screen.exitonclick()