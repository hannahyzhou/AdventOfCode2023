# Advent of Code
# December 6th

# two lists, where index is the game number and the value is either race_time or min_distance
# counter i starting at 0, where i represents the amount of time you hold the button. race_time - i will be the time the boat has to move
# i will also be the speed (mm/ms) that the boat will travel. Distance traveled will be i * (race_time - i)
# if distance_traveled is > min_distance for that race, add i to a list of winning_i's 
# append list of winning_i's to total list of winning_i's
# take length of each list of winning_i's and multiply it together at the end


### PART 1

total_winning_i = []

with open ('12_6_2023_input.txt', 'r') as f:
    race_times_string = f.readline()
    race_times_list = [substring.split() for substring in race_times_string.split(":")][1]
    min_distances_string = f.readline()
    min_distances_list = [substring.split() for substring in min_distances_string.split(":")][1]
    
    for race_num in range(len(race_times_list)): # for each race
        i = 0 # i represents the amount of time you hold the button, and also the speed (mm/ms) the boat will travel
        # print("race number: ", race_num)
        winning_i = []
        while i < int(race_times_list[race_num]):
            distance_traveled = i * (int(race_times_list[race_num]) - i)
            # print("i: ", i, "\t", "distance traveled: ", distance_traveled)
            if distance_traveled > int(min_distances_list[race_num]):
                winning_i.append(i)
            i+=1
        total_winning_i.append(winning_i)

product = 1
for winning_i in total_winning_i:
    product *= len(winning_i)

print(product)


### PART 2

with open ('12_6_2023_input.txt', 'r') as f:
    race_time_string = f.readline()
    race_time = race_time_string.split(":")[1]
    race_time = int(race_time.replace(" ", ""))
    min_distance_string = f.readline()
    min_distance = min_distance_string.split(":")[1]
    min_distance = int(min_distance.replace(" ", ""))
    print("race time: ", race_time)
    print("min distance: ", min_distance)
    
    i = 1 # i represents the amount of time you hold the button, and also the speed (mm/ms) the boat will travel
    # print("race number: ", race_num)
    winning_i = []
    while i < race_time:
        distance_traveled = i * (race_time - i)
        # print("i: ", i, "\t", "distance traveled: ", distance_traveled)
        if distance_traveled > min_distance:
            winning_i.append(i)
        i+=1

print(len(winning_i))