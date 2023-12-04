import re
puzzle_input = []
with open("input.txt") as file:
    puzzle_input = file.read().strip().split('\n')

def part1():
    id_sum = 0
    for line in puzzle_input:
        id = int(re.search(r"(?<=Game )\d+(?=:)", line).group(0))
        red = 0
        green = 0
        blue = 0

        for subset in line.split(";"):
            red_search = re.search(r"\d+(?= red)", subset)
            green_search = re.search(r"\d+(?= green)", subset)
            blue_search = re.search(r"\d+(?= blue)", subset)
            if red_search:
                red = max(red, int(red_search.group(0)))
            if green_search:
                green = max(green, int(green_search.group(0)))
            if blue_search:
                blue = max(blue, int(blue_search.group(0)))

        if red <= 12 and green <= 13 and blue <= 14:
            id_sum += id
    print(id_sum)

def part2():
    power_sum = 0
    for line in puzzle_input:
        red = 0
        green = 0
        blue = 0

        for subset in line.split(";"):
            red_search = re.search(r"\d+(?= red)", subset)
            green_search = re.search(r"\d+(?= green)", subset)
            blue_search = re.search(r"\d+(?= blue)", subset)
            if red_search:
                red = max(red, int(red_search.group(0)))
            if green_search:
                green = max(green, int(green_search.group(0)))
            if blue_search:
                blue = max(blue, int(blue_search.group(0)))

        power_sum += red * green * blue
    print(power_sum)

if __name__ == "__main__":
    part1()
    part2()