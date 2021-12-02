import re
import os
import sys

dataset = []
with open(os.path.join(sys.path[0], "2021day1input.txt")) as f:
    dataset = list(map(int, f.read().split('\n')))
    
def part1(input):
    increase = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            increase += 1
    return increase

def part2(input):
    increase = 0
    for i in range(3, len(input)):
        if input[i] > input[i - 3]:
            increase += 1
    return increase