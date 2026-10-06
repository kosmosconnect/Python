# Class 5 - while and for loops

# while: start, condition, update
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print("Done!")               # 1 2 3 4 5 Done!

# range(start, stop, step) - the stop is never included
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(1, 6)))      # [1, 2, 3, 4, 5]
print(list(range(1, 11, 2)))  # [1, 3, 5, 7, 9]
print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]

# for: multiplication table
n = 7
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
