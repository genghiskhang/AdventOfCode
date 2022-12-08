import pathlib
from collections import defaultdict
test_case = []
with open("2022day7input.txt") as file:
    test_case = list(map(str, file.read().split("\n")))

def part1(): #1182909
    directories = []
    for line in range(1, len(test_case[:20])):
        isDirectory = False
        directory = ""
        directory_items = {}
        if "$ ls" in test_case[line]:
            directory = test_case[line - 1].split()[2]
            print(directory)
            directory_items.update({directory:[]})
            isDirectory = True
        if isDirectory:
            start_line = line + 1
            while "$" not in test_case[start_line] and start_line < len(test_case) :
                directory_items[directory].append((test_case[start_line], test_case[start_line].split()[2])["dir" in test_case[start_line]])
                start_line += 1
            directories.append(directory_items)
    print(directories)
    if test_case[line] == "$ ls":
        if "$ cd" not in test_case[line - 1]:
            print("fk", line)
    # iterate through test_case
    # every cd that is not .., increase level by one
    # every cd that is .., decrease level by one
    # cd / set level to 0
    # level = 0
    # cmds = [" ".join(line.split()[1:]) for line in test_case[:30] if "$" in line]
    # dirs = [line.split()[1] for line in test_case[:30] if "dir" in line]
    # for line in test_case:
    #     pass

    # print(cmds)
    # print(dirs)


    # SZ = defaultdict(int)
    # path = []
    # for line in test_case:
    #     words = line.strip().split()
    #     if words[1] == 'cd':
    #         if words[2] == '..':
    #             path.pop()
    #         else:
    #             path.append(words[2])
    #     elif words[1] == 'ls':
    #         continue
    #     else:
    #         try:
    #             sz = int(words[0])
    #             for i in range(len(path) + 1):
    #                 SZ['/'.join(path[:i])] += sz
    #         except:
    #             pass
    # max_used = 70000000 - 30000000
    # total_used = SZ['/']
    # need_to_free = total_used - max_used
    # best = 1e9
    # ans = 0
    # for k,v in SZ.items():
    #     if v >= need_to_free:
    #         best = min(best, v)
    #     if v <= 100000:
    #         ans += v
    # print(ans)

def part2(): #2832508
    pass
    # SZ = defaultdict(int)
    # path = []
    # for line in test_case:
    #     words = line.strip().split()
    #     if words[1] == 'cd':
    #         if words[2] == '..':
    #             path.pop()
    #         else:
    #             path.append(words[2])
    #     elif words[1] == 'ls':
    #         continue
    #     elif words[0] == 'dir':
    #         continue
    #     else:
    #         sz = int(words[0])
    #         for i in range(1, len(path) + 1):
    #             SZ['/'.join(path[:i])] += sz

    # max_used = 70000000 - 30000000
    # total_used = SZ['/']
    # need_to_free = total_used - max_used
    # p1 = 0
    # p2 = 1e9
    # for k,v in SZ.items():
    #     if v <= 100000:
    #         p1 += v
    #     if v>=need_to_free:
    #         p2 = min(p2, v)
    # print(p1)
    # print(p2)

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()