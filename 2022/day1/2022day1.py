import pathlib
test_case = []
with open("2022day1input.txt") as file:
    test_case = list(map(str, file.read().split("\n")))

def part1():
    global_max = 0
    local_max = 0
    for cal in test_case:
        if cal != "":
            local_max += int(cal)
        else:
            if local_max > global_max:
                global_max = local_max
            local_max = 0
    return global_max

def part2():
    local_max = 0
    top3 = [0, 0, 0]
    for cal in test_case:
        if cal != "":
            local_max += int(cal)
        else:
            if local_max > top3[-1]:
                top3[-1] = local_max
            local_max = 0
            top3.sort(reverse=True)
    return sum(top3)

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()