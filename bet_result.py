
class GetResult:
    def __init__(self, turtles_rating, players):
        sorted_values_of_turtle = sorted(turtles_rating.items(), key=lambda item: item[1])
        print("*****   Here Is The Bet Result   *****")

        first_position = False
        for keys in players:
            if players[keys] == sorted_values_of_turtle[0][0]:
                print(f"{keys} got the first position")
                first_position = True
        if not first_position:
            print(f"{sorted_values_of_turtle[0][0]}"
                  f" got the first position")

        second_position = False
        for keys in players:
            if players[keys] == sorted_values_of_turtle[1][0]:
                print(f"{keys} got the second position")
                second_position = True
        if not second_position:
            print(f"{sorted_values_of_turtle[1][0]}"
                  f" got the second position")

        if len(players) >= 3:
            third_position = False
            for keys in players:
                if players[keys] == sorted_values_of_turtle[2][0]:
                    print(f"{keys} got the third position")
                    third_position = True
            if not third_position:
                print(f"{sorted_values_of_turtle[2][0]}"
                      f" got the third position")