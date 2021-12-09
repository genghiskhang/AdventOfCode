import re
import os
import sys

dataset = []
with open(os.path.join(sys.path[0], "2021day2input.txt")) as f:
    dataset = f.read().split('\n')
    
def part1(input):
    horiz = 0
    depth = 0
    for i in range(len(input)):
        if re.search(r'(?<=forward\W)\d', input[i]):
            horiz += int(re.findall(r'(?<=forward\W)\d', input[i])[0])
        if re.search(r'(?<=up\W)\d', input[i]):
            depth -= int(re.findall(r'(?<=up\W)\d', input[i])[0])
        if re.search(r'(?<=down\W)\d', input[i]):
            depth += int(re.findall(r'(?<=down\W)\d', input[i])[0])
    return horiz * depth

def part2(input):
    horiz = 0
    depth = 0
    aim = 0
    for i in range(len(input)):
        if re.search(r'(?<=forward\W)\d', input[i]):
            horiz += int(re.findall(r'(?<=forward\W)\d', input[i])[0])
            depth += aim * int(re.findall(r'(?<=forward\W)\d', input[i])[0])
        if re.search(r'(?<=up\W)\d', input[i]):
            aim -= int(re.findall(r'(?<=up\W)\d', input[i])[0])
        if re.search(r'(?<=down\W)\d', input[i]):
            aim += int(re.findall(r'(?<=down\W)\d', input[i])[0])
    return horiz * depth