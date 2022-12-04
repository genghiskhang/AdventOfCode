import pathlib
test_case = []
with open("2022day4input.txt") as file:
    test_case = list(map(str, file.read().split("\n")))

def part1():
    contained = 0
    for pair in test_case:
        e1_start = int(pair.split(",")[0].split("-")[0])
        e1_end = int(pair.split(",")[0].split("-")[1])
        e2_start = int(pair.split(",")[1].split("-")[0])
        e2_end = int(pair.split(",")[1].split("-")[1])
        if (e1_start <= e2_start and e1_end >= e2_end) or (e2_start <= e1_start and e2_end >= e1_end):
            contained += 1
    return contained

def part2():
    overlap = 0
    for pair in test_case:
        e1_start = int(pair.split(",")[0].split("-")[0])
        e1_end = int(pair.split(",")[0].split("-")[1])
        e2_start = int(pair.split(",")[1].split("-")[0])
        e2_end = int(pair.split(",")[1].split("-")[1])
        if ((e1_start <= e2_end and e1_start >= e2_start) or (e1_end <= e2_end and e1_end >= e2_start)) or ((e2_start <= e1_end and e2_start >= e1_start) or (e2_end <= e1_end and e2_end >= e1_start)):
            overlap += 1
    return overlap

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()