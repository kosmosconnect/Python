# Class 6 practice - answers

n = int(input("Size: "))

# Task 1: n by n square
for i in range(n):
    print("* " * n)

# Task 2: 1 / 2 2 / 3 3 3 / 4 4 4 4
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

# Task 3: primes from 2 to 50
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# Task 4: perfect number (sum of factors below n equals n)
num = int(input("Number: "))
total = 0
for i in range(1, num):
    if num % i == 0:
        total += i
if total == num and num > 0:
    print(num, "is a perfect number")      # 6, 28
else:
    print(num, "is not a perfect number")

# Bonus: hollow square
for r in range(n):
    for c in range(n):
        if r == 0 or r == n - 1 or c == 0 or c == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
