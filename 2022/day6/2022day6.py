import pathlib
test_case = []
with open("2022day6input.txt") as file:
    test_case = file.readline().strip()

def part1():
    last4 = []
    char_count = 0
    for c in test_case:
        if len(last4) < 4:
            last4.append(c)
        else:
            flag = False
            each = last4.copy()
            each.sort()
            for x in range(len(each) - 1):
                if each[x] == each[x + 1]:
                    flag = True
            if not flag:
                break
            last4 = last4[1:]
            last4.append(c)
        char_count += 1
    return char_count

def part2():
    last14 = []
    char_count = 0
    for c in test_case:
        if len(last14) < 14:
            last14.append(c)
        else:
            flag = False
            each = last14.copy()
            each.sort()
            for x in range(len(each) - 1):
                if each[x] == each[x + 1]:
                    flag = True
            if not flag:
                break
            last14 = last14[1:]
            last14.append(c)
        char_count += 1
    return char_count

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()