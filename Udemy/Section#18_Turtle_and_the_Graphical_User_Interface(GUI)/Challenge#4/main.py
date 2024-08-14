import turtle as t
import random



tim = t.Turtle()


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")
for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))