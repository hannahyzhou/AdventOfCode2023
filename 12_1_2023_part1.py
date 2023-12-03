# Advent of Code 2023
# December 1st

# iterate through string
# is_first_num flag - set True to begin with, then false once you find a number
# store first_num and last_num, and update the last_num with each new digit found. 
# for debugging purposes: store all calibration numbers in a list, then add the list up at the end. Otherwise can just o a running sum

calibration_nums = []

with open('calibration_doc.txt', 'r') as f:
    for line in f: # for each line
        is_first_num = True
        first_num = 0
        last_num = 0
        print("line: " + line)
        for char in line: # for each character in each line
            if char.isnumeric():
                if is_first_num is True: # if this is the first digit seen
                    first_num = int(char)
                    last_num = int(char)
                    is_first_num = False
                else:
                    last_num = int(char)
            print((first_num*10) + last_num)
        calibration_nums.append((first_num * 10) + last_num)

print("calibration_nums list: ")
print(calibration_nums)
sum = 0
for calib_num in calibration_nums:
    sum += calib_num

print("Final sum: ")
print(sum)
