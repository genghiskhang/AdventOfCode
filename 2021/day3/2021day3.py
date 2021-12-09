import os
import sys

dataset = []
with open(os.path.join(sys.path[0], "2021day3input.txt")) as f:
    dataset = f.read().split('\n')
    
def part1(input):
    gamma = ''
    epsilon = ''
    for i in range(len(input[0])):
        bin = 0
        for j in range(len(input)):
            bin += int(input[j][i])
        if bin >= int(len(input) / 2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)

def part2(input):
    oxygen = input
    co2 = input
    for i in range(len(oxygen[0])):
        if len(oxygen) == 1:
            break
        ones = []
        zeros = []
        for j in range(len(oxygen)):
            if int(oxygen[j][i]) == 1:
                ones.append(oxygen[j])
            else:
                zeros.append(oxygen[j])
        if len(ones) >= len(zeros):
            oxygen = ones
        else:
            oxygen = zeros
    for i in range(len(co2[0])):
        if len(co2) == 1:
            break
        ones = []
        zeros = []
        for j in range(len(co2)):
            if int(co2[j][i]) == 1:
                ones.append(co2[j])
            else:
                zeros.append(co2[j])
        if len(ones) >= len(zeros):
            co2 = zeros
        else:
            co2 = ones
    return int(co2[0], 2) * int(oxygen[0], 2)