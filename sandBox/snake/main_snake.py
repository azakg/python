from turtle import Turtle, Screen
from snakeSnake import Snake
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")

snake = Snake()


game_is_on = True
while game_is_on:


screen.exitonclick()

