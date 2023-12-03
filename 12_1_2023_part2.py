# Advent of Code 2023
# December 1st

# keep a list of valid digits/words
valid_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# for each line, keep a first_num and last_num again
# also keep an earliest_position and latest_position, earliest_position initialized to infinity, latest_position initialized to earliest
# iterate through valid_digits and see where each one can be found in the line (if -1, then not found in line).
# if one is found smaller than earliest_position or bigger than latest_position, update them accordingly

calibration_nums = []

def convert_word_to_digit(word):
    if word == "one": word = "1"
    elif word == "two": word = "2"
    elif word == "three": word = "3"
    elif word == "four": word = "4"
    elif word == "five": word = "5"
    elif word == "six": word = "6"
    elif word == "seven": word = "7"
    elif word == "eight": word = "8"
    else: word = "9"
    return word

with open('calibration_doc.txt', 'r') as f:
    for line in f: # for each line
        is_first_num_found = True
        first_num = 0
        last_num = 0
        earliest_position = float('inf')
        latest_position = float('inf')
        for digit in valid_digits: # iterating through the valid digits list
            found_position = line.find(digit) # earliest instance found
            greatest_found_position = line.rfind(digit) # latest instance found
            if found_position != -1: # if this digit is in the string
                # checks for earliest instance found
                if found_position < earliest_position:
                    if not digit.isnumeric(): # if the digit found is not numeric
                        digit = convert_word_to_digit(digit)
                    first_num = int(digit) # updating the first number
                    earliest_position = found_position
                    if is_first_num_found: # if this is the first number found, temporarily set it also to the latest_position so that it is initialized to something
                        if not digit.isnumeric(): digit = convert_word_to_digit
                        latest_position = earliest_position
                        last_num = int(digit)
                        is_first_num_found = False
                elif found_position > latest_position:
                    if not digit.isnumeric(): # if the digit found is not numeric
                        digit = convert_word_to_digit(digit)
                    last_num = int(digit) # updating the last number
                    latest_position = found_position
                # checks for latest instance found
                if greatest_found_position < earliest_position:
                    if not digit.isnumeric(): # if the digit found is not numeric
                        digit = convert_word_to_digit(digit)
                    first_num = int(digit) # updating the first number
                    earliest_position = greatest_found_position
                    if is_first_num_found: # if this is the first number found, temporarily set it also to the latest_position so that it is initialized to something
                        if not digit.isnumeric(): digit = convert_word_to_digit
                        latest_position = earliest_position
                        last_num = int(digit)
                        is_first_num_found = False
                elif greatest_found_position > latest_position:
                    if not digit.isnumeric(): # if the digit found is not numeric
                        digit = convert_word_to_digit(digit)
                    last_num = int(digit) # updating the last number
                    latest_position = greatest_found_position
        calibration_nums.append((first_num * 10) + last_num)

print("calibration_nums list: ")
print(calibration_nums)
sum = 0
for calib_num in calibration_nums:
    sum += calib_num

print("Final sum: ")
print(sum)
                

