import re
import os
import sys

dataset = []
with open(os.path.join(sys.path[0], "2020day4input.txt")) as f:
    dataset = f.read().split('\n\n')
  
def part1(input):
    valid = 0
    for i in range(len(input)):
        if 'byr' in input[i] and 'iyr' in input[i] and 'eyr' in input[i] and 'hgt' in input[i] and 'hcl' in input[i] and 'ecl' in input[i] and 'pid' in input[i]:
            valid += 1
    return valid

def part2(input):
    CHECKS = 7
    valid = 0
    
    byr_regex = r'(?<=byr:)\d{4}'# four digits, 1920-2002
    iyr_regex = r'(?<=iyr:)\d{4}'# four digits, 2010-2020
    eyr_regex = r'(?<=eyr:)\d{4}'# four digits, 2020-2030
    hgt_in_regex = r'(?<=hgt:)\d+(?=in)'# num followed by 59-76in
    hgt_cm_regex = r'(?<=hgt:)\d+(?=cm)'# num followed by 150-193cm
    hcl_regex = r'(?<=hcl:)#[0-9a-f]{6}'# # followed by six digit hexadecimal
    ecl_regex = r'(?<=ecl:)(amb|blu|brn|gry|grn|hzl|oth)'# amb blu brn gry grn hzl oth
    pid_regex = r'(?<=pid:)\d{9}\b'# nine digit including leading zeros
    
    for i in range(len(input)):
        check = 0
        if re.search(byr_regex, input[i]) and int(re.findall(byr_regex, input[i])[0]) >= 1920 and int(re.findall(byr_regex, input[i])[0]) <= 2002:
            check += 1
        if re.search(iyr_regex, input[i]) and int(re.findall(iyr_regex, input[i])[0]) >= 2010 and int(re.findall(iyr_regex, input[i])[0]) <= 2020:
            check += 1
        if re.search(eyr_regex, input[i]) and int(re.findall(eyr_regex, input[i])[0]) >= 2020 and int(re.findall(eyr_regex, input[i])[0]) <= 2030:
            check += 1
        if (re.search(hgt_in_regex, input[i]) and int(re.findall(hgt_in_regex, input[i])[0]) >= 59 and int(re.findall(hgt_in_regex, input[i])[0]) <= 76) or (re.search(hgt_cm_regex, input[i]) and int(re.findall(hgt_cm_regex, input[i])[0]) >= 150 and int(re.findall(hgt_cm_regex, input[i])[0]) <= 193):
            check += 1 
        if re.search(hcl_regex, input[i]):
            check += 1
        if re.search(ecl_regex, input[i]):
            check += 1
        if re.search(pid_regex, input[i]):
            check += 1
        if check == CHECKS:
            valid += 1
    return valid