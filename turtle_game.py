from Turtle_Racer import Racers, turtle_color
from Player import PlayerNumber
from turtle import Turtle, Screen
import random

class TurtleGame:
    def __init__(self):
        self.count_of_players = int(input("How many players do you have? (1-6) ==>\n"))
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Turtle Race")
        self.turtle = []
        self.players = {}
        self.turtles_rating = {}
        self.is_race_on = False


    def start_playing(self):
        self.number_of_players()
        self.turtle = Racers(self.count_of_players)

    def number_of_players(self):
        for numbers in range(self.count_of_players):
            player_name = self.screen.textinput(title=f"{numbers + 1} player's name",
                prompt="What is your name?").title()
            bet_color = self.screen.textinput(title="Make your bet",
                prompt=f"Which turtle your are betting on:"
                       f" {turtle_color[0:self.count_of_players]}: ").lower()
            self.players[f"{player_name}"] = bet_color