import re

def part1(input):
    valid = 0
    for i in range(len(input)):
        min = int(re.findall('\d+', input[i])[0])
        max = int(re.findall('\d+', input[i])[1])
        target = re.findall('\w(?=:)', input[i])[0]
        pw = re.findall('(?<=:\W)\w+', input[i])[0]
        if pw.count(target) >= min and pw.count(target) <= max:
            valid += 1
    return valid

def part2(input):
    valid = 0
    for i in range(len(input)):
        min = int(re.findall('\d+', input[i])[0])
        max = int(re.findall('\d+', input[i])[1])
        target = re.findall('\w(?=:)', input[i])[0]
        pw = re.findall('(?<=:\W)\w+', input[i])[0]
        if (pw[min - 1] == target) ^ (pw[max - 1] == target):
            valid += 1
    return valid
print(part2(dataset))