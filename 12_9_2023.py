# Advent of Code 2023
# December 9th

# list of extrapolated values
extrapolated_values = []
extrapolated_values_backwards = []
filename = '12_9_2023_input_small.txt'


# input: original list of numbers
# output: returns the number to add to the last element of the original list of numberss
def next_number_add(list_numbers):
    # base case
    if all(element == 0 for element in list_numbers):
        return 0
    else:
        # take list_differences
        list_differences = [second - first for first, second in zip(list_numbers, list_numbers[1:])]
        # return list_differences.last() + next_number(list_differences)
        return list_differences[-1] + next_number_add(list_differences)

# input: original list of numbers
# output: returns the number to subtract from the first element of the original list of numbers
def next_number_subtract(list_numbers):
    # base case
    if all(element == 0 for element in list_numbers):
        return 0
    else:
        # take list_differences
        list_differences = [second - first for first, second in zip(list_numbers, list_numbers[1:])]
        # return list_differences.last() + next_number(list_differences)
        return list_differences[0] - next_number_subtract(list_differences)
    

def part1():
    # iterate through each line
    with open (filename, 'r') as f:
        # go through each line
        for line in f:
            list_numbers = [int(num) for num in line.split()]
            next_number = list_numbers[-1] + next_number_add(list_numbers)
            extrapolated_values.append(next_number)

    print("extrapolated values: ", extrapolated_values)
    print("sum of extrapoalted values: ", sum(extrapolated_values))

def part2():
    # iterate through each line
    with open (filename, 'r') as f:
        # go through each line
        for line in f:
            list_numbers = [int(num) for num in line.split()]
            next_number = list_numbers[0] - next_number_subtract(list_numbers)
            extrapolated_values_backwards.append(next_number)

    print("extrapolated values backwards: ", extrapolated_values_backwards)
    print("sum of extrapoalted values backwards: ", sum(extrapolated_values_backwards))


# RUN EITHER PART 1 OR PART 2 HERE
# part1()
part2()
        
        


