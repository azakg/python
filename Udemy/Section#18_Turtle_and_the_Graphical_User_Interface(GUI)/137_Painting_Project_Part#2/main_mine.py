import turtle as t
import random

rgb_colors = [(199, 175, 117), (124, 36, 24),
              (210, 221, 213), (168, 106, 57),
              (186, 158, 53), (6, 57, 83), (109, 67, 85),
              (113, 161, 175), (22, 122, 174), (64, 153, 138),
              (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177), (176, 198, 203),
              (150, 115, 120), (202, 185, 190), (40, 72, 82),
              (46, 73, 62), (47, 66, 82)]


tim = t.Turtle()
t.colormode(255)
#tim.pencolor(255,255,255)
x = -0
y = -360
tim.penup()
tim.hideturtle()
tim.speed('fastest')
dot_size = 20

for _ in range(20):
    y += 35
    x = -335
    for _ in range(20):
        tim.setpos(x, y)
        tim.dot(dot_size, random.choice(rgb_colors))
        x += 35
        #tim.goto(60, 0)



screen =t.Screen()
screen.exitonclick()