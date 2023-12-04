puzzle_input = []
with open("input.txt") as file:
    puzzle_input = file.read().strip().split('\n')

def part1():
    sum = 0
    num = ""
    hasSymbol = False
    for r in range(len(puzzle_input)):
        for c in range(len(puzzle_input[r])):
            if puzzle_input[r][c].isnumeric():
                if num == "":
                    if r - 1 >= 0 and c - 1 >= 0:
                        if not puzzle_input[r - 1][c - 1].isnumeric() and puzzle_input[r - 1][c - 1] != ".":
                            hasSymbol = True
                    if c - 1 >= 0:
                        if not puzzle_input[r][c - 1].isnumeric() and puzzle_input[r][c - 1] != ".":
                            hasSymbol = True
                    if r + 1 < len(puzzle_input) and c - 1 >= 0:
                        if not puzzle_input[r + 1][c - 1].isnumeric() and puzzle_input[r + 1][c - 1] != ".":
                            hasSymbol = True
                if r - 1 >= 0:
                    if not puzzle_input[r - 1][c].isnumeric() and puzzle_input[r - 1][c] != ".":
                        hasSymbol = True
                if r + 1 < len(puzzle_input):
                    if not puzzle_input[r + 1][c].isnumeric() and puzzle_input[r + 1][c] != ".":
                        hasSymbol = True

                num += puzzle_input[r][c]
                        
                if (c + 1 == len(puzzle_input[r]) and num != "") or (c + 1 < len(puzzle_input[r]) and not puzzle_input[r][c + 1].isnumeric()):
                    if r - 1 >= 0 and c + 1 < len(puzzle_input[r]):
                        if not puzzle_input[r - 1][c + 1].isnumeric() and puzzle_input[r - 1][c + 1] != ".":
                            hasSymbol = True
                    if c + 1 < len(puzzle_input[r]):
                        if not puzzle_input[r][c + 1].isnumeric() and puzzle_input[r][c + 1] != ".":
                            hasSymbol = True
                    if r + 1 < len(puzzle_input) and c + 1 < len(puzzle_input[r]):
                        if not puzzle_input[r + 1][c + 1].isnumeric() and puzzle_input[r + 1][c + 1] != ".":
                            hasSymbol = True
                    
                    if hasSymbol:
                        sum += int(num)

                    num = ""
                    hasSymbol = False
    print(sum)

def part2():
    gears = {}
    total_ratio = 0
    num = ""
    curr_gears = []
    for r in range(len(puzzle_input)):
        for c in range(len(puzzle_input[r])):
            if puzzle_input[r][c].isnumeric():
                if num == "":
                    if r - 1 >= 0 and c - 1 >= 0:
                        if puzzle_input[r - 1][c - 1] == "*":
                            gear_pos = f"[{r - 1},{c - 1}]"
                            if gear_pos not in curr_gears:
                                curr_gears.append(gear_pos)
                    if c - 1 >= 0:
                        if puzzle_input[r][c - 1] == "*":
                            gear_pos = f"[{r},{c - 1}]"
                            if gear_pos not in curr_gears:
                                curr_gears.append(gear_pos)
                    if r + 1 < len(puzzle_input) and c - 1 >= 0:
                        if puzzle_input[r + 1][c - 1] == "*":
                            gear_pos = f"[{r + 1},{c - 1}]"
                            if gear_pos not in curr_gears:
                                curr_gears.append(gear_pos)
                if r - 1 >= 0:
                    if puzzle_input[r - 1][c] == "*":
                        gear_pos = f"[{r - 1},{c}]"
                        if gear_pos not in curr_gears:
                            curr_gears.append(gear_pos)
                if r + 1 < len(puzzle_input):
                    if puzzle_input[r + 1][c] == "*":
                        gear_pos = f"[{r + 1},{c}]"
                        if gear_pos not in curr_gears:
                            curr_gears.append(gear_pos)

                num += puzzle_input[r][c]
                        
                if (c + 1 == len(puzzle_input[r]) and num != "") or (c + 1 < len(puzzle_input[r]) and not puzzle_input[r][c + 1].isnumeric()):
                    if r - 1 >= 0 and c + 1 < len(puzzle_input[r]):
                        if puzzle_input[r - 1][c + 1] == "*":
                            gear_pos = f"[{r - 1},{c + 1}]"
                            if gear_pos not in curr_gears:
                                curr_gears.append(gear_pos)
                    if c + 1 < len(puzzle_input[r]):
                        if puzzle_input[r][c + 1] == "*":
                            gear_pos = f"[{r},{c + 1}]"
                            if gear_pos not in curr_gears:
                                curr_gears.append(gear_pos)
                    if r + 1 < len(puzzle_input) and c + 1 < len(puzzle_input[r]):
                        if puzzle_input[r + 1][c + 1] == "*":
                            gear_pos = f"[{r + 1},{c + 1}]"
                            if gear_pos not in curr_gears:
                                curr_gears.append(gear_pos)
                    
                    for gear in curr_gears:
                        if gear not in gears:
                            gears[gear] = []
                        gears[gear].append(int(num))

                    num = ""
                    curr_gears = []

    for key in gears.keys():
        if len(gears[key]) > 1:
            ratio = 1
            for gear in gears[key]:
                ratio *= gear
            total_ratio += ratio
    print(total_ratio)

if __name__ == "__main__":
    part1()
    part2()