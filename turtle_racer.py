from turtle import Turtle

turtle_position = [-80, -40, 0, 40, 80, 120]
turtle_color = ["red", "green", "blue", "black", "brown", "orange"]

class Racers:
    def __init__(self, players_numbers):
        self.turtles = []
        self.turtle_racers(players_numbers)
    def turtle_racers(self, players_numbers):
        for number in range(players_numbers):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(turtle_color[number])
            new_turtle.penup()
            new_turtle.goto(-300, y=turtle_position[number])
            self.turtles.append(new_turtle)