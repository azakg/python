import turtle
from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.addSegment()
        score.increase_score()

    #Detect collision with wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x >= 300 or x <= -300 and x >= 300 or x <= -300:
        score.gameOverText()
        break
    if y >= 300 or y <= -300 and y >= 300 or y <= -300:
        score.gameOverText()
        break


    #Detect_collision_with_body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameOverText()



screen.exitonclick()