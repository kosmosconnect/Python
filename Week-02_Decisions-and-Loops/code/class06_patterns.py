# Class 6 - nested loops and patterns

# Rectangle: 3 rows, 4 columns
for row in range(1, 4):
    for col in range(1, 5):
        print("*", end=" ")
    print()
print()

n = 4

# Right triangle
for i in range(1, n + 1):
    print("* " * i)
print()

# Same triangle with a nested loop (some exams want this version)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Upside down
for i in range(n, 0, -1):
    print("* " * i)
print()

# Centred pyramid
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)
print()

# Counting rows: 1 / 1 2 / 1 2 3 / 1 2 3 4
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()

# Floyd's triangle
num = 1
for i in range(1, 4):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
