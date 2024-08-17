from turtle import Turtle, Screen
import random

#tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
list_of_turtles = []
list_of_colors = ['red', 'blue', 'green', 'brown', 'purple']
x = -200
y = -200

finish = False


for number in range(5):
    #turtle = Turtle()
    list_of_turtles.append(Turtle())
    turtle = list_of_turtles[number]
    turtle.shape('turtle')
    print(number)
    turtle.color(list_of_colors[number])
    turtle.penup()
    y += 60
    turtle.goto(x, y)


print(list_of_turtles[0])

while not finish:
    turtle_num = random.randint(0,4)
    random_turtle = list_of_turtles[turtle_num]
    random_turtle.forward(1)

screen.exitonclick()