from turtle import Turtle, Screen
from Turtle_Racer import Racers

class PlayerNumber:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Turtle Race")
    def number_of_players(self):
        count_of_players = int(self.screen.textinput(title="Number of Players", prompt="How many players do you have?"))
        for numbers in range(count_of_players):
            player_name = self.screen.textinput(title=f"{numbers +1} player's name", prompt="What is your name?").title()
            bet_color = self.screen.textinput(title="Make your bet", prompt=f"Which turtle your are betting on: {turtle_color[0:count_of_players]}: ").lower()
            self.players[f"{player_name}"] = bet_color
        Turtle_Racers.Racer(count_of_players)