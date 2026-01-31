from turtle import Turtle

position = [-80, -40, 0, 40, 80, 120]
turtle_color = ["red", "green", "blue", "black", "brown", "orange"]

class Racers:
    def preparing_fields(self, players_numbers):
        for number in range(players_numbers):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(turtle_color[number])
            new_turtle.penup()
            new_turtle.goto(-300, y=position[number])
            self.turtles.append(new_turtle)