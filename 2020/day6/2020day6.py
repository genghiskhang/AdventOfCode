import re
import os
import sys

dataset = []
with open(os.path.join(sys.path[0], "2020day6input.txt")) as f:
    dataset = f.read().split('\n\n')
    
def part1(input):
    answers = 0
    for i in range(len(input)):
        unique = []
        for j in range(len(input[i])):
            if input[i][j] not in unique and input[i][j] != '\n':
                unique.append(input[i][j])
        answers += len(unique)
    return answers

def part2(input):
    answers = 0
    
    return answers