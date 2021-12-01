import re
import os
import sys

dataset = []
with open(os.path.join(sys.path[0], "2020day5input.txt")) as f:
    dataset = f.read().split('\n')
    
def part1(input):
    maxID = 0
    for i in range(len(input)):
        fb = re.findall(r'[F|B]+', input[i])[0]
        lr = re.findall(r'[L|R]+', input[i])[0]
        row = [0, 127]
        col = [0, 7]
        rowNum = 0
        colNum = 0
        
        for j in range(len(fb) - 1):
            if fb[j] == 'F':
                row[1] -= int((row[1] - row[0]) / 2) + 1
            elif fb[j] == 'B':
                row[0] += int((row[1] - row[0]) / 2) + 1
        if fb[len(fb) - 1] == 'F':
            rowNum = row[0]
        elif fb[len(fb) - 1] == 'B':
            rowNum = row[1]
        
        for j in range(len(lr) - 1):
            if lr[j] == 'L':
                col[1] -= int((col[1] - col[0]) / 2) + 1
            elif lr[j] == 'R':
                col[0] += int((col[1] - col[0]) / 2) + 1
        if lr[len(lr) - 1] == 'L':
            colNum = col[0]
        elif lr[len(lr) - 1] == 'R':
            colNum = col[1]
        print(rowNum * 8 + colNum)
        if rowNum * 8 + colNum > maxID:
            maxID = rowNum * 8 + colNum
    return maxID

def part2(input):
    id = 0
    idList = []
    for i in range(len(input)):
        fb = re.findall(r'[F|B]+', input[i])[0]
        lr = re.findall(r'[L|R]+', input[i])[0]
        row = [0, 127]
        col = [0, 7]
        rowNum = 0
        colNum = 0
        
        for j in range(len(fb) - 1):
            if fb[j] == 'F':
                row[1] -= int((row[1] - row[0]) / 2) + 1
            elif fb[j] == 'B':
                row[0] += int((row[1] - row[0]) / 2) + 1
        if fb[len(fb) - 1] == 'F':
            rowNum = row[0]
        elif fb[len(fb) - 1] == 'B':
            rowNum = row[1]
        
        for j in range(len(lr) - 1):
            if lr[j] == 'L':
                col[1] -= int((col[1] - col[0]) / 2) + 1
            elif lr[j] == 'R':
                col[0] += int((col[1] - col[0]) / 2) + 1
        if lr[len(lr) - 1] == 'L':
            colNum = col[0]
        elif lr[len(lr) - 1] == 'R':
            colNum = col[1]
            
        idList.append(rowNum * 8 + colNum)
    idList.sort()
    for i in range(1, len(idList)):
        if not idList[i] - idList[i - 1] == 1:
            id = idList[i] - 1
    return id