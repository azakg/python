import sys
import turtle as t
import random
tim = t.Turtle()


colors = ['green', 'blue', 'red', 'black', 'maroon', 'indigo', 'pink', 'bisque']
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
#
# t.done()

go_on = True
countDown = 100
tim.pensize(10)
while go_on:
    tim.color(random.choice(colors))
    tim.forward(30)
    turn = random.randint(1, 3)
    if turn == 1:
        tim.right(90)
    elif turn == 2:
        tim.left(90)
    elif turn == 3:
        tim.backward(60)
    countDown -= 1
    if countDown < 1:
        go_on = False

