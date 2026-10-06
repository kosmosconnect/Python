# Class 14 practice - answers

# Task 1: min and max together
def min_max(nums):
    small = big = nums[0]
    for n in nums:
        if n < small:
            small = n
        if n > big:
            big = n
    return small, big

lo, hi = min_max([34, 78, 12, 91, 56])
print(lo, hi)                                  # 12 91

# Task 2: sort by length
print(sorted(["Puri", "Bhubaneswar", "Cuttack"], key=len))

# Task 3: odd numbers with filter and lambda
print(list(filter(lambda n: n % 2 == 1, range(1, 21))))

# Task 4: grade function (see code/class14_records_functions.py for it in use)
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    return "F"

for a in [95, 80, 61, 45, 20]:
    print(a, grade(a))
