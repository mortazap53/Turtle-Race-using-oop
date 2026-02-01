from turtle import Screen

position = [-80, -40, 0, 40, 80, 120]
turtle_color = ["red", "green", "blue", "black", "brown", "orange"]

class PlayerNumber:
    def __init__(self, player):
        self.players_names = player
    def number_of_players(self, players_names):
        count_of_players = int(self.screen.textinput(title="Number of Players", prompt="How many players do you have?"))
        for numbers in range(count_of_players):
            player_name = self.screen.textinput(title=f"{numbers +1} player's name", prompt="What is your name?").title()
            bet_color = self.screen.textinput(title="Make your bet", prompt=f"Which turtle your are betting on: {turtle_color[0:count_of_players]}: ").lower()
            players_names[f"{player_name}"] = bet_color
