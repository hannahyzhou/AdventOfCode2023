# Advent of Code 2023
# December 2nd
# Part 2

# Create a hash map for each game where key is the color and value is the highest count of that color in that game

NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14
game_powers_list = []

with open('games.txt', 'r') as f:
    for line in f: # for each game
        power_of_game = 1
        colors_max = {"red" : 0, "green" : 0, "blue" : 0} #initialize these for each game

        two_list = line.split(":")
        first_half = two_list[0].split()
        id_num = first_half[1]
        print("game number: " + id_num)
        games_string = two_list[1].strip()
        print("game: " + games_string)
        rounds_list = [game.strip() for game in games_string.split(";")] # creates list where each item is a round in the game
        for round in rounds_list: # for each round
            is_round_possible = True
            colors_list = [color.strip() for color in round.split(",")]
            for color in colors_list:
                words_list = color.split()
                words_list.reverse() # creates list that looks like: ["green", "15", "red", "2"]
                color = words_list[0]
                quantity = int(words_list[1])
                if color == "red":
                    if quantity > colors_max["red"]: colors_max["red"] = quantity
                if color == "green":
                    if quantity > colors_max["green"]: colors_max["green"] = quantity
                if color == "blue":
                    if quantity > colors_max["blue"] : colors_max["blue"] = quantity   
        print(colors_max)
        for value in colors_max.values():
            power_of_game = power_of_game * value
        game_powers_list.append(power_of_game)   
        print("power of game " + id_num + ": " + str(power_of_game))          
        print("\n") 

sum = 0
for power in game_powers_list:
    sum += power
print(sum)

