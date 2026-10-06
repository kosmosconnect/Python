# Class 23 practice - answers

# Task 2: Selection sort
nums = [64, 25, 12, 22, 11]
for i in range(len(nums)):
    small = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[small]:
            small = j
    nums[i], nums[small] = nums[small], nums[i]
print(nums)                                    # [11, 12, 22, 25, 64]

# Task 3: count the checks
def linear_checks(nums, target):
    checks = 0
    for x in nums:
        checks += 1
        if x == target:
            break
    return checks

def binary_checks(nums, target):
    low, high, checks = 0, len(nums) - 1, 0
    while low <= high:
        checks += 1
        mid = (low + high) // 2
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return checks

print("Linear:", linear_checks(nums, 64))      # 5
print("Binary:", binary_checks(nums, 64))      # 3

big = list(range(1, 1001))
print("1000 items -> linear:", linear_checks(big, 1000),
      "binary:", binary_checks(big, 1000))
