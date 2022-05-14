import turtle
from turtle import Turtle, Screen
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
districts_to_list = districts.District.to_list()
print(districts_to_list)

screen.exitonclick()
