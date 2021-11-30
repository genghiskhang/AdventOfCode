def part1(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if not i == j:
                if nums[i] + nums[j] == target:
                    return nums[i] * nums[j]
                
def part2(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if not i == j and not j == k and not k == i:
                    if nums[i] + nums[j] + nums[k] == target:
                        return nums[i] * nums[j] * nums[k]