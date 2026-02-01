from game import Game

turtle_color = ["red", "green", "blue", "black", "brown", "orange"]
turtle_position = [30, -30, 90, -90, 150, -150]
count_of_players = int(input("How many players do you have? (2-6)\n==> "))
if __name__ == '__main__':
    game = Game(players_number=count_of_players,
                      turtles_positions=turtle_position,
                      turtles_colors=turtle_color)
    game.play_game()