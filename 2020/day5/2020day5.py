import re
import os
import sys

dataset = []
with open(os.path.join(sys.path[0], "2020day5input.txt")) as f:
    dataset = f.read().split('\n')
    
def part1(input):
    maxID = 0
    for i in range(len(input)):
        seatRange = [0, 127]
        rowRange = [0, 7]
        index = 0
        row = 0
        while input[i][index] == 'F' or input[i][index] == 'B':
            if input[i][index] == 'F':
                seatRange[1] -= int((seatRange[1] - seatRange[0]) / 2) + 1
            elif input[i][index] == 'B':
                seatRange[0] += int((seatRange[1] - seatRange[0]) / 2) + 1
            index += 1
        
    return maxID

def part2(input):
    pass

part1(dataset)