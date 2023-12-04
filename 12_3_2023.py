# Advent of Code 2023
# December 3rd

# convert engine schematic (strings) to a 2d array
# iterate through each character of each line. If current index is a digit, start recording what number it is until not a digit
# make sure to stop before out of bounds
# for each number have is_part_number flag, initially set to false until an adjacent symbol is reached. then set to true
# if by the end of the number, is_part_number flag is true, add to list of part numbers
# sum part numbers

# input: line number, current index in line
# output: returns true if adjacent_squares contain symbol, false if not
def check_adjacent_squares(l, i):
    # CHECKING LEFT, RIGHT, UP, DOWN
    if i < LINE_LENGTH - 1: # not the rightmost character
        if not schematic_array[l][i+1].isnumeric() and schematic_array[l][i+1] != '.': # if not a number and not a .
            return True
    if i > 0: # if not the leftmost character
        if not schematic_array[l][i-1].isnumeric() and schematic_array[l][i-1] != '.':
            return True
    if l < NUMBER_LINES - 1: # not the last line
        if not schematic_array[l+1][i].isnumeric() and schematic_array[l+1][i] != '.':
            return True
    if l > 0: # if not the first line
        if not schematic_array[l-1][i].isnumeric() and schematic_array[l-1][i] != '.':
            return True
    # CHECKING DIAGONALS
    if i < LINE_LENGTH - 1 and l < NUMBER_LINES - 1: # checking the bottom right diagonal
        if not schematic_array[l+1][i+1].isnumeric() and schematic_array[l+1][i+1] != '.':
            return True
    if i > 0 and l < NUMBER_LINES - 1: # checking the bottom left diagonal
        if not schematic_array[l+1][i-1].isnumeric() and schematic_array[l+1][i-1] != '.':
            return True
    if i < LINE_LENGTH - 1 and l > 0: # checking the top right diagonal
        if not schematic_array[l-1][i+1].isnumeric() and schematic_array[l-1][i+1] != '.':
            return True
    if i > 0 and l > 0 : # checking the top left diagonal
        if not schematic_array[l-1][i-1].isnumeric() and schematic_array[l-1][i-1] != '.':
            return True
    return False # if no adjacent/diagonal squares are symbol, return false

schematic_array = []
part_number_list = []

LINE_LENGTH = 0 # each row is a line, row length is the num of characters in each line
NUMBER_LINES = 0 # number of lines there are in the schematic


with open ('engine_schematic.txt', 'r') as f:
    for line in f:
        LINE_LENGTH = len(line) #should be the same for all rows
        NUMBER_LINES += 1
        row = []
        for char in line: # for each character in the line
            if char is not '\n': row.append(char)
        schematic_array.append(row)

i = 0 # current index in the line
l = 0 # what number line in the file

# traversing left to right, up to down

while l < NUMBER_LINES:
    while i < LINE_LENGTH:
        if schematic_array[l][i].isnumeric():
            is_part_number = False
            curr_number = schematic_array[l][i] # initialize the current number to the first digit seen
            is_part_number = check_adjacent_squares(l, i)
            while i < LINE_LENGTH-1 and schematic_array[l][i].isnumeric():
                if is_part_number is True: # if we know it's a part number
                    while i < LINE_LENGTH-1 and schematic_array[l][i].isnumeric(): # keep iterating
                        i+=1
                        curr_number += schematic_array[l][i]
                    # after it's found the full number
                    part_number_list.append(curr_number)
                    curr_number = 0 # reset current number to 0
                else: # if not yet discovered
                    while i < LINE_LENGTH-1 and schematic_array[l][i].isnumeric(): # keep iterating
                        i+=1
                        curr_number += schematic_array[l][i]

                



