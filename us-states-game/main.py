import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("US State's Game")
screen.addshape(image)
turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
print(states)
answers = []
score = 0
while score<50:
    answer_state = screen.textinput(title="Guess the State",prompt="what's the another state name").title()
    print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in states:
        answers.append(answer_state)
        score+=1
        screen.title(f"{score}/50 states correct")
        # index = states.index(answer_state)
        # x_cor = x[index]
        # y_cor = y[index]
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

#unguessed states
un_states = [state for state in states if state not in answers]
# for state in states:
#     if state not in answers:
#         un_states.append(state)


pandas.DataFrame(un_states).to_csv("missed_states")

