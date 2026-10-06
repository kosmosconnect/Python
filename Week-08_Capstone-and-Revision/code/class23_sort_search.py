# Class 23 - bubble sort and binary search

nums = [64, 25, 12, 22, 11]
n = len(nums)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)                                  # [11, 12, 22, 25, 64]


def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(nums, 25))               # 3
print(binary_search(nums, 99))               # -1

# Predict-the-output answers from the slide
print(7 // 2, 7 % 2)                         # 3 1
print("Hi" * 2 + "!")                        # HiHi!
print(list(range(2, 9, 3)))                  # [2, 5, 8]
print("Python"[1:4])                         # yth
print(len({1, 2, 2, 3}))                     # 3
print(bool(""), bool("0"))                   # False True
print(10 / 5)                                # 2.0
