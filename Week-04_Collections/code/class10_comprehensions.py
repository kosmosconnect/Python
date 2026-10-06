# Class 10 - list comprehensions

# The long way
sq = []
for x in range(1, 6):
    sq.append(x * x)
print(sq)                                   # [1, 4, 9, 16, 25]

# The short way
sq = [x * x for x in range(1, 6)]
print(sq)

nums = [34, 78, 12, 91]
print([n * 2 for n in nums])                # [68, 156, 24, 182]
print([n for n in nums if n > 50])          # [78, 91]
print([n % 10 for n in nums])               # [4, 8, 2, 1]
print([n // 10 for n in nums])              # [3, 7, 1, 9]
print([c.upper() for c in "odia"])          # ['O', 'D', 'I', 'A']

# Read many numbers typed on one line, e.g. 10 20 30
values = [int(x) for x in input("Numbers: ").split()]
print(values, "sum =", sum(values))
