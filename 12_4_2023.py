# Advent of Code
# December 4th

### PART 1


# separate input starting from after the colon using .split(":") and also .strip() to remove trailing whitespace
# separate input by "|"
# separate input by spaces on left side to get winning numbers
# keep winning number input as a dictionary, iterate through the rightside numbers to see if any of them are 'in' the dictionary
# flag for if first winning number, set to true initially. Set to false once first winning number is found
# if first winning number, game points = 1, else * 2
# add points to a list
# sum up points at the end

game_points_list = []

with open ('12_4_2023_txt.txt', 'r') as f:
    for line in f:
        is_first_win = True
        game_points = 0
        two_split = [part.strip() for part in line.split(":")]
        game_string = two_split[1] # second half is what we need
        game_string_split = [part.strip() for part in game_string.split("|")]
        winning_numbers_list = game_string_split[0].split() # list of winning numbers
        winning_numbers_dict = {winning_number : None for winning_number in winning_numbers_list} # adding all winning numbers to a dictionary
        my_numbers = game_string_split[1].split() # list of my numbers
        for my_number in my_numbers:
            if my_number in winning_numbers_dict and is_first_win:
                is_first_win = False
                game_points = 1
            elif my_number in winning_numbers_dict and not is_first_win:
                game_points = game_points * 2
            else: 
                continue
        game_points_list.append(game_points)

sum = 0
for game_points in game_points_list:
    sum += game_points
print(sum)


### PART 2
# hash table where key is the game number, value is the list of copies won from that game
# separate list of copies won, add to the list whenever a copy of a game is won. Pop from the list until nothing is left
# running count of number of scratchcards (originals + copies)

total_copies_won_list = []
copies_won_dict = {} # key is game number, value is a list of copies won from that game
number_scratchcards_won = 0

with open ('12_4_2023_txt.txt', 'r') as f:
    for line in f:
        two_split = [part.strip() for part in line.split(":")]
        game_id = two_split[0].split()[1]
        game_string = two_split[1]
        temp_num_copies_won = 0
        temp_copies_won_list = []
        game_string_split = [part.strip() for part in game_string.split("|")]
        winning_numbers_list = game_string_split[0].split() # list of winning numbers
        winning_numbers_dict = {winning_number : None for winning_number in winning_numbers_list} # adding all winning numbers to a dictionary
        my_numbers = game_string_split[1].split() # list of my numbers
        for my_number in my_numbers:
            if my_number in winning_numbers_dict:
                temp_num_copies_won += 1
        for i in range(1,temp_num_copies_won+1):
            total_copies_won_list.append(int(game_id) + i)
            temp_copies_won_list.append(int(game_id) + i)
        copies_won_dict[int(game_id)] = temp_copies_won_list
        number_scratchcards_won += 1

while total_copies_won_list: #while there are still copies to process
    curr_copy_game_id = total_copies_won_list.pop()
    number_scratchcards_won += 1
    total_copies_won_list.extend(copies_won_dict[curr_copy_game_id])

print(number_scratchcards_won)


        



        
