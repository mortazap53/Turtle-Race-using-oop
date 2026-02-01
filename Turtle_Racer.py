from turtle import Turtle
from turtle_game import turtle_position, turtle_color

class Racers:
    def __init__(self, players_numbers):
        for number in range(players_numbers):
            self.new_turtle = Turtle(shape="turtle")
            self.new_turtle.color(turtle_color[number])
            self.new_turtle.penup()
            self.new_turtle.goto(-300, y=turtle_position[number])