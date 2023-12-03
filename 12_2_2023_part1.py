# Advent of Code 2023
# December 2nd
# Part 1

NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14
possible_game_ids = []

with open('games.txt', 'r') as f:
    for line in f: # for each game
        is_game_possible = True
        two_list = line.split(":")
        first_half = two_list[0].split()
        id_num = first_half[1]
        print("game number: " + id_num)
        games_string = two_list[1].strip()
        print("game: " + games_string)
        rounds_list = [game.strip() for game in games_string.split(";")] # creates list where each item is a round in the game
        for round in rounds_list:
            is_round_possible = True
            print("new round")
            colors_list = [color.strip() for color in round.split(",")]
            for color in colors_list:
                words_list = color.split()
                words_list.reverse() # creates list that looks like: ["green", "15", "red", "2"]
                color = words_list[0]
                quantity = int(words_list[1])
                if color == "red":
                    if quantity > NUM_RED:
                        is_round_possible = False
                        break
                if color == "green":
                    if quantity > NUM_GREEN: 
                        is_round_possible = False
                        break
                if color == "blue":
                    if quantity > NUM_BLUE:
                        is_round_possible = False
                        break
            if is_round_possible == False:
                is_game_possible = False
                break #if round is impossible, skip the rest of the rounds in the game
        if is_game_possible: possible_game_ids.append(int(id_num))                  
        print("\n")
    print(possible_game_ids)

sum = 0
for id in possible_game_ids:
    sum += id
print(sum)

