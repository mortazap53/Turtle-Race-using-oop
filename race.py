import random

class Run:
    def __init__(self, players, turtles):
        self.turtles_rating = {}
        for values in players.values():
            if values:
                self.is_race_on = True
                self.run(turtles)

    def run(self, turtles):
        while self.is_race_on:
            for turtle in turtles:
                color = turtle.pencolor()
                self.turtles_rating[color] = turtle.xcor()
                if turtle.xcor() > 350:
                    self.is_race_on = False
                random_step = random.randint(0,10)
                turtle.forward(random_step)