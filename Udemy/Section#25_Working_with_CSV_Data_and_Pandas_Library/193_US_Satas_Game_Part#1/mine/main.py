import turtle
import pandas
from turtle import Turtle
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.setup(760, 560)
screen.bgpic(image)

states = pandas.read_csv("50_states.csv")

states_dic = states.to_dict()
print(states_dic)

def checkAnswer(answer):

    for i in range(50):
        if answer == states_dic['state'][i]:
            name = states_dic['state'][i]
            x = states_dic['x'][i]
            y = states_dic['y'][i]
            print(x)
            print(y)
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.setposition(x, y)
    turtle.write(name, font=('Verdana', 10, 'normal'))



game_is_on = True
while game_is_on:
    answer = screen.textinput("Welcome to US State game!", "Are you ready?").title()
    checkAnswer(answer)

screen.exitonclick()