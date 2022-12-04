import pathlib
test_case = []
with open("2022day2input.txt") as file:
    test_case = list(map(str, file.read().split("\n")))

def part1():
    score = 0
    move_score = {
        "X":1,
        "Y":2,
        "Z":3
    }
    outcome_score = {
        "win":6,
        "lose":0,
        "tie":3
    }
    winning_moves = {
        "A":"Y",
        "B":"Z",
        "C":"X"
    }
    moves = {
        "A":"X",
        "B":"Y",
        "C":"Z"
    }
    for round in test_case:
        opp_move = round[0]
        your_move = round[-1]
        if your_move == winning_moves[opp_move]:
            score += outcome_score["win"]
        elif your_move == moves[opp_move]:
            score += outcome_score["tie"]
        else:
            score += outcome_score["lose"]
        score += move_score[your_move]
    return score

def part2():
    score = 0
    move_score = {
        "X":1,
        "Y":2,
        "Z":3
    }
    outcome_score = {
        "X":0,
        "Y":3,
        "Z":6
    }
    correct_move = {
        "X":{
            "A":"Z",
            "B":"X",
            "C":"Y"
        },
        "Y":{
            "A":"X",
            "B":"Y",
            "C":"Z"
        },
        "Z":{
            "A":"Y",
            "B":"Z",
            "C":"X"
        }
    }
    for round in test_case:
        opp_move = round[0]
        your_move = round[-1]
        score += move_score[correct_move[your_move][opp_move]]
        score += outcome_score[your_move]
    return score

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()