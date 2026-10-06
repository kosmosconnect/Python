# Class 10 - 2D lists (matrices)

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(m[0])                  # [1, 2, 3]
print(m[1][2])               # 6
print(len(m), len(m[0]))     # 3 3

# Every cell, with row sums
for row in m:
    for x in row:
        print(x, end=" ")
    print("| sum =", sum(row))

# Index version: the diagonal
print("Diagonal:", [m[i][i] for i in range(3)])   # [1, 5, 9]

# Matrix addition
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print(C)                     # [[6, 8], [10, 12]]
