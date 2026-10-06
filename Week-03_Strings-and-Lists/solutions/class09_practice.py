# Class 9 practice - answers

# Task 1: How many above average
marks = []
for i in range(5):
    marks.append(int(input("Marks: ")))
avg = sum(marks) / len(marks)
above = 0
for m in marks:
    if m > avg:
        above += 1
print(f"Average {avg:.1f}, above average: {above}")

# Task 2: Second largest (one loop, no sorting)
nums = [34, 78, 12, 91]
big, second = nums[0], nums[1]
if second > big:
    big, second = second, big
for n in nums[2:]:
    if n > big:
        second = big
        big = n
    elif n > second:
        second = n
print("Second largest:", second)             # 78

# Task 3: Remove repeats
items = [1, 2, 2, 3, 1]
unique = []
for x in items:
    if x not in unique:
        unique.append(x)
print(unique)                                # [1, 2, 3]

# Task 4: Evens and odds
nums = [11, 4, 7, 20, 15, 8]
evens, odds = [], []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)
print("Evens:", evens, "Odds:", odds)
