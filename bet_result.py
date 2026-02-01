
class GetResult:
    def __init__(self, turtles_rating, players):
        sorted_values_of_turtle = sorted(turtles_rating.items(), key=lambda item: item[1], reverse=True)
        print("*****   Here Is The Bet Result   *****")
        for keys in players:
            if players[keys] == sorted_values_of_turtle[0][0]:
                print(f"{keys} got the first position!")
        for keys in players:
            if players[keys] == sorted_values_of_turtle[1][0]:
                print(f"{keys} got the second position!")
        if len(players) >= 3:
            for keys in players:
                if players[keys] == sorted_values_of_turtle[2][0]:
                    print(f"{keys} got the third position!")