import turtle
from turtle import Turtle, Screen

import pandas
import pandas as pd

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Bangladesh district game")

# Loading up the image of Bangladesh
image = "Bangladesh_map.gif"
screen.addshape(image)
turtle.shape(image)

# Reading the districts from the .csv file
districts = pd.read_csv("bd_districts.csv")
print(districts)
# Turning the districts from .csv to list
all_districts = districts.District.to_list()
# print(all_districts)


# Getting axis in Map

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Game mechanics
guessed_districts = []

while len(guessed_districts) < 50:
    answer = screen.textinput(title=f"{len(guessed_districts)}/64 district guessed correctly",
                              prompt="What's the next district?").title()

    if answer == "Exit":
        break
    if answer in all_districts:
        guessed_districts.append(answer)
        coordinates = districts[districts.District == answer]
        x_cor = int(coordinates.x)
        y_cor = int(coordinates.y)
        timmy = Turtle()
        timmy.ht()
        timmy.penup()
        timmy.goto(x_cor, y_cor)
        timmy.write(answer)
        all_districts.remove(answer)

screen.exitonclick()

remaining_districts = pandas.DataFrame(all_districts)
remaining_districts.to_csv("Remaining Districts")
