from turtle import Turtle, Screen
import random

position = [-80, -40, 0, 40, 80, 120]
turtle_color = ["red", "green", "blue", "black", "brown", "orange"]

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Turtle Race")
        self.turtles = []
        self.players = {}
        self.turtles_rating = {}
        self.is_race_on = False