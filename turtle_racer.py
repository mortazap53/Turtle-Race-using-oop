from turtle import Turtle
import random

class MakingRacers:

    def __init__(self, count_of_players, turtle_color, turtle_position):
        self.turtles = []
        self.turtle_color = turtle_color
        self.turtle_position = turtle_position
        self.making_turtle_racers(players_numbers=count_of_players)

    def making_turtle_racers(self, players_numbers):
        for number in range(players_numbers):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(self.turtle_color[number])
            new_turtle.penup()
            yposition = random.choice(self.turtle_position)
            new_turtle.goto(-300, y=yposition)
            self.turtles.append(new_turtle)
            self.turtle_position.remove(yposition)