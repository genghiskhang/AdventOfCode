import pathlib
import regex as re
test_case = []
with open("input.txt") as file:
    test_case = file.read().strip().split('\n')

def part1():
    sum = 0
    for line in test_case:
        digits = re.findall(r"\d", line)
        sum += int(digits[0] + digits[-1])
    print(sum)

def part2():
    nums = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    sum = 0
    for line in test_case:
        num = ""
        digits = re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True)
        if digits[0] in nums:
            num += nums[digits[0]]
        else:
            num += digits[0]
        if digits[-1] in nums:
            num += nums[digits[-1]]
        else:
            num += digits[-1]
        sum += int(num)
    print(sum)
    
if __name__ == "__main__":
    part1()
    part2()