# Class 10 practice - answers

# Task 1: Diagonal sum of a 3 by 3 matrix (type each row like: 1 2 3)
m = []
for i in range(3):
    m.append([int(x) for x in input(f"Row {i + 1}: ").split()])
total = 0
for i in range(3):
    total += m[i][i]
print("Diagonal sum:", total)

# Task 2: Transpose
m = [[1, 2, 3], [4, 5, 6]]
t = []
for j in range(3):
    row = []
    for i in range(2):
        row.append(m[i][j])
    t.append(row)
print(t)                                    # [[1, 4], [2, 5], [3, 6]]

# Task 3: Even squares
print([x * x for x in range(1, 11) if x % 2 == 0])   # [4, 16, 36, 64, 100]

# Task 4: Largest in each row
marks = [[78, 85, 92], [65, 70, 88], [90, 61, 75]]
for row in marks:
    print(row, "->", max(row))
