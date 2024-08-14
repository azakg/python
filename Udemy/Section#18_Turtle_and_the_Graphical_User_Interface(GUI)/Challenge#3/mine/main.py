import turtle
from turtle import Turtle, Screen
from draw import Draw
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

drawer = Draw(tim)
color_list = ['cyan', 'deep pink', 'lime', 'red', 'blue violet']
for i in range(3, 11):
    drawer.drawFigure(i,)
    tim.color(random.choice(color_list))

screen = Screen()
screen.exitonclick()