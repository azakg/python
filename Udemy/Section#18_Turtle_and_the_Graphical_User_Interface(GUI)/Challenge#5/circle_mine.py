import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
angle = 10


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(36):
    tim.circle(100)
    tim.color(random_color())
    tim.right(angle)

screen = t.Screen()
screen.exitonclick()