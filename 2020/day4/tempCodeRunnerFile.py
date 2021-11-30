r_regex, input[i]) and int(re.findall(byr_regex, input[i])[0]) >= 1920 and int(re.findall(byr_regex, input[i])[0]) <= 2002:
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