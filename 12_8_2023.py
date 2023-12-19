# Advent of Code 2023
# December 8th

# data structure for each element which has a left and right component
class element:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "left: " + self.left + "\t" + "right: " + self.right

filename = '12_8_2023_input_large.txt'

# have to read in the entire file first?
# add to a dictionary of elements where the key is the name (ex: AAA) and the value is the data structure
elements_list = {}
directions = ""
with open (filename, 'r') as f:
    # read first two lines: first line is list of directions, second line is empty
    directions = f.readline()
    directions = directions[:-1] # extra character at the end?
    f.readline() # empty line
    for line in f:
        equals_split = [substring.strip() for substring in line.split("=")]
        name = equals_split[0] # name of element
        element_directions = [substring.strip() for substring in equals_split[1].split(",")]
        element_directions[0] = element_directions[0][1:]
        element_directions[1] = element_directions[1][:-1]
        elements_list[name] = element(element_directions[0], element_directions[1])

num_directions = len(directions)
counter = 0
i = 0
path = []
curr_element = 'AAA' # start at AAA

while curr_element != 'ZZZ':
    print(curr_element)
    next_direction = directions[i % num_directions]
    if next_direction == "L": # if go left
        next_element = elements_list[curr_element].left
    else: # if go right
        next_element = elements_list[curr_element].right
    # proceed to next step
    curr_element = next_element
    counter += 1
    i += 1
    path.append(curr_element)

print("steps taken to get to ZZZ: ", i)

