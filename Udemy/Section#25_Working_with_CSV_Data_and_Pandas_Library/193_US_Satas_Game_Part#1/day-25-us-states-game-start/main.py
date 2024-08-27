import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states )}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    #If answer_state is one of the states in alll the states of the 50_state.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        #IF they got it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == answer_state]
        t.goto(state_date.x.item(), state_date.y.item())
            #Create a turtle to write the name of the state at the state's x and y coordate

        #Next two lines do same thing, you can choose eather the first or the second
        t.write(answer_state)
        #t.write(state_date.state.item())

# states_to_learn.csv
rest_states = []
for i in range(len(all_states) -1, len(guessed_states), -1):
    rest_states.append(all_states[i])


df = pandas.DataFrame(rest_states)
df.to_csv("rest_states.csv")