# Class 5 practice - answers

# Task 1: Times table
n = int(input("Table of: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Task 2: Count digits
num = int(input("Number: "))
count = 0
if num == 0:
    count = 1
while num > 0:
    count += 1
    num //= 10
print("Digits:", count)                # 90210 -> 5

# Task 3: Armstrong (3 digits)
num = int(input("3-digit number: "))
original = num
total = 0
while num > 0:
    d = num % 10
    total += d ** 3
    num //= 10
if total == original:
    print(original, "is an Armstrong number")    # 153
else:
    print(original, "is not an Armstrong number")

# Task 4: Sum of even numbers from 1 to n
n = int(input("n: "))
total = 0
for i in range(2, n + 1, 2):
    total += i
print("Even sum:", total)              # n = 10 -> 30
