import turtle
from turtle import Turtle, Screen
import pandas as pd


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Bangladesh district game")

# Lodaing up the image of Bangladesh
image = "b.gif"
screen.addshape(image)
turtle.shape(image)

screen.exitonclick()
