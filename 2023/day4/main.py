import regex as re
from collections import defaultdict
puzzle_input = []
with open("input.txt") as file:
    puzzle_input = file.read().strip().split('\n')

def part1():
    total_points = 0
    for card in puzzle_input:
        card = re.sub(r"Card\s+\d+: ", "", card)
        winning = [int(i.strip()) for i in card.split("|")[0].split()]
        yours = [int(i.strip()) for i in card.split("|")[1].split()]

        matches = 0
        for your in yours:
            if your in winning:
                matches += 1
        if matches > 0:
            total_points += 2**(matches - 1)
    print(total_points)

def part2():
    N = defaultdict(int)
    for i, line in enumerate(puzzle_input):
        N[i] += 1
        first, rest = line.split('|')
        id, card = first.split(":")
        card_nums = [int(x) for x in card.split()]
        rest_nums = [int(x) for x in rest.split()]
        val = len(set(card_nums) & set(rest_nums))
        for j in range(val):
            N[i + 1 + j] += N[i]
    print(sum(N.values()))
    # total_scartchcards = 0
    # card_counts = {}

    # i = 0
    # for card in puzzle_input:
    #     print(i)
    #     if i in card_counts:
    #         for _ in range(card_counts[i]):
    #             card = re.sub(r"Card\s+\d+: ", "", card)
    #             winning = [int(i.strip()) for i in card.split("|")[0].split()]
    #             yours = [int(i.strip()) for i in card.split("|")[1].split()]

    #             matches = 0
    #             for your in yours:
    #                 if your in winning:
    #                     matches += 1

    #             if matches > 0:
    #                 print("match: ", matches)
    #                 print(sorted(winning), sorted(yours))
                
    #             for m in range(1, matches + 1):
    #                 if i + m not in card_counts:
    #                     card_counts[i + m] = 0
    #                 card_counts[i + m] += 1
    #     else:
    #         card = re.sub(r"Card\s+\d+: ", "", card)
    #         winning = [int(i.strip()) for i in card.split("|")[0].split()]
    #         yours = [int(i.strip()) for i in card.split("|")[1].split()]

    #         matches = 0
    #         for your in yours:
    #             if your in winning:
    #                 matches += 1
            
    #         for m in range(1, matches + 1):
    #             if i + m not in card_counts:
    #                 card_counts[i + m] = 0
    #             card_counts[i + m] += 1
        
    #     i += 1

    # for k in card_counts.keys():
    #     if k < len(puzzle_input):
    #         total_scartchcards += card_counts[k]
    # print(card_counts)

    # print(total_scartchcards)

if __name__ == "__main__":
    part1()
    part2()