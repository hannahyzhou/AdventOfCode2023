# Advent of Code 2023
# December 3rd

### PART 1

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

possible_part_squares = []

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

print("LINE LENGTH: ", LINE_LENGTH)
print("NUMBER LINES: ", NUMBER_LINES)

# creating the possible_part_squares array
for l in range(NUMBER_LINES):
    temp_row = []
    for i in range(LINE_LENGTH):
        is_possible_part_square = check_adjacent_squares(l, i)
        if is_possible_part_square:
            temp_row.append(True)
        else: temp_row.append(False)
    possible_part_squares.append(temp_row)

# DEBUGGING: print array of possible parts squares
for i in range(NUMBER_LINES):
    for j in range(LINE_LENGTH):
        if possible_part_squares[i][j]:
            print("!", end = " ")
        else: print(".", end = " ")
    print('\n')


i = 0 # current index in the line
l = 0 # what number line in the file

# # traversing left to right, up to down

while l < NUMBER_LINES: # while indices are in bounds
    print("l: ", l)
    while i < NUMBER_LINES:
        print("i: ", i)
        is_part_number = False
        if schematic_array[l][i].isnumeric(): # if found a number?
            curr_number = ""
            while i < NUMBER_LINES and schematic_array[l][i].isnumeric(): # continue iterating until non numeric or OOB
                curr_number += schematic_array[l][i] # add digit to current number
                if possible_part_squares[l][i]: # if current digit is adjacent to a symbol
                    is_part_number = True
                i+=1
            print(curr_number)
            if is_part_number: part_number_list.append(curr_number)
            curr_number = "" # clear the current number
            i+=1
        else: i+=1
    i=0
    l+=1

sum = 0
for part_number in part_number_list:
    sum += int(part_number)
print(sum)
        



                



