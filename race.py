import random

class Run:
    def __init__(self, players, turtles):
        self.is_race_on = False
        self.turtles_rating = {}
        self.check_values(players, turtles)

    def check_values(self, players, turtles):
        for values in players.values():
            if values:
                self.is_race_on = True
                self.run(turtles_on_field=turtles)

    def run(self, turtles_on_field):
        while self.is_race_on:
            for turtle in turtles_on_field:
                color = turtle.pencolor()
                self.turtles_rating[color] = turtle.xcor()
                if turtle.xcor() > 350:
                    turtle.setheading(180)
                if turtle.xcor() < -350:
                    self.is_race_on = False
                random_step = random.randint(0,10)
                turtle.forward(random_step)