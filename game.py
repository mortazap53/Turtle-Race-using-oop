from turtle_racer import MakingRacers
from bet_result import GetResult
from turtle import Screen
from race import Run

class TurtleGame:
    def __init__(self, players_number, turtles_positions, turtles_colors):
        self.positions = turtles_positions
        self.colors = turtles_colors
        self.players_number = players_number
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Turtle Race")
        self.players = {}
        self.object_turtles = None
        self.object_race = None
        self.object_get_result = None


    def start_playing(self):
        self.object_turtles = MakingRacers(count_of_players=self.players_number,
                                    turtle_position=self.positions,
                                    turtle_color=self.colors)
        self.number_of_players()
        self.object_race = Run(players=self.players,
                        turtles=self.object_turtles.turtles)
        self.object_get_result = GetResult(turtles_rating=self.object_race.turtles_rating,
                                    players=self.players)
        self.keep_screen()


    def number_of_players(self):
        for numbers in range(self.players_number):
            player_name = self.screen.textinput(title=f"{numbers + 1} player's name",
                prompt="What is your name?").title()
            bet_color = self.screen.textinput(title="Make your bet",
                prompt=f"Which turtle your are betting on:"
                       f"{self.object_turtles.turtle_color[0:self.players_number]}: ").lower()
            self.players[f"{player_name}"] = bet_color

    def keep_screen(self):
       self.screen.exitonclick()