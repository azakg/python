from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle(shape='square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(position)
    new_segment.speed('slowest')
    segments.append(new_segment)




game_is_on = True
while game_is_on:
    #screen.update()
    for seg in reversed(segments):
        seg.forward(60)

        #time.sleep(1)










screen.exitonclick()