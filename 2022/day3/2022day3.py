import pathlib
test_case = []
with open("2022day3input.txt") as file:
    test_case = list(map(str, file.read().split("\n")))

def part1():
    priority = 0
    for sack in test_case:
        comp1 = sack[:int(len(sack) / 2)]
        comp2 = sack[int(len(sack) / 2):]
        odd = ""
        for item in comp1:
            if item in comp2:
                odd = item
        priority += (ord(odd.lower()) - ord("a") + 1) + ((26, 0)[odd.islower()])
    return priority

def part2():
    priority = 0
    groups = []
    for i in range(0, len(test_case), 3):
        groups.append(test_case[i:i + 3])
    for group in groups:
        key = ""
        for item in group[0]:
            if item in group[1] and item in group[2]:
                key = item
        priority += (ord(key.lower()) - ord("a") + 1) + ((26, 0)[key.islower()])
    return priority

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()