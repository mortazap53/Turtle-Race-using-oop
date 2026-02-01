from turtle_racer import Racers, turtle_color
from bet_result import GetResult
from turtle import Screen
from race import Run

class TurtleGame:
    def __init__(self):
        self.count_of_players = int(input("How many players do you have? (1-6)\n==> "))
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Turtle Race")
        self.turtles = []
        self.players = {}
        self.is_race_on = False
        self.race = None
        self.get_result = None


    def start_playing(self):
        self.number_of_players()
        self.turtles = Racers(self.count_of_players).turtles
        self.race = Run(self.players, self.turtles)
        self.get_result = GetResult(self.race.turtles_rating, self.players)
        self.keep_screen()


    def number_of_players(self):
        for numbers in range(self.count_of_players):
            player_name = self.screen.textinput(title=f"{numbers + 1} player's name",
                prompt="What is your name?").title()
            bet_color = self.screen.textinput(title="Make your bet",
                prompt=f"Which turtle your are betting on:"
                       f" {turtle_color[0:self.count_of_players]}: ").lower()
            self.players[f"{player_name}"] = bet_color

    def keep_screen(self):
       self.screen.exitonclick()