#             [M] [S] [S]            
#         [M] [N] [L] [T] [Q]        
# [G]     [P] [C] [F] [G] [T]        
# [B]     [J] [D] [P] [V] [F] [F]    
# [D]     [D] [G] [C] [Z] [H] [B] [G]
# [C] [G] [Q] [L] [N] [D] [M] [D] [Q]
# [P] [V] [S] [S] [B] [B] [Z] [M] [C]
# [R] [H] [N] [P] [J] [Q] [B] [C] [F]
#  1   2   3   4   5   6   7   8   9

import pathlib
test_case = []
with open("2022day5input.txt") as file:
    test_case = list(map(str, file.read().split("\n")))

def part1():
    top_crates = ""
    starting_config = [
        ["R", "P", "C", "D", "B", "G"],
        ["H", "V", "G"],
        ["N", "S", "Q", "D", "J", "P", "M"],
        ["P", "S", "L", "G", "D", "C", "N", "M"],
        ["J", "B", "N", "C", "P", "F", "L", "S"],
        ["Q", "B", "D", "Z", "V", "G", "T", "S"],
        ["B", "Z", "M", "H", "F", "T", "Q"],
        ["C", "M", "D", "B", "F"],
        ["F", "C", "Q", "G"]
    ]
    for instruction in test_case:
        num_crates = int(instruction.split(" ")[1])
        move_from = int(instruction.split(" ")[3]) - 1
        move_to = int(instruction.split(" ")[5]) - 1

        for n in range(num_crates):
            if len(starting_config[move_from]) == 0:
                break
            starting_config[move_to].append(starting_config[move_from].pop(-1))
    for crates in starting_config:
        top_crates += crates[-1]
    return top_crates

def part2():
    top_crates = ""
    starting_config = [
        ["R", "P", "C", "D", "B", "G"],
        ["H", "V", "G"],
        ["N", "S", "Q", "D", "J", "P", "M"],
        ["P", "S", "L", "G", "D", "C", "N", "M"],
        ["J", "B", "N", "C", "P", "F", "L", "S"],
        ["Q", "B", "D", "Z", "V", "G", "T", "S"],
        ["B", "Z", "M", "H", "F", "T", "Q"],
        ["C", "M", "D", "B", "F"],
        ["F", "C", "Q", "G"]
    ]
    for instruction in test_case:
        num_crates = int(instruction.split(" ")[1])
        move_from = int(instruction.split(" ")[3]) - 1
        move_to = int(instruction.split(" ")[5]) - 1

        starting_config[move_to] += starting_config[move_from][-num_crates:]
        starting_config[move_from] = starting_config[move_from][:-num_crates]
    for crates in starting_config:
        top_crates += crates[-1]
    return top_crates

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()