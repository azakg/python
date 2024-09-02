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
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
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

