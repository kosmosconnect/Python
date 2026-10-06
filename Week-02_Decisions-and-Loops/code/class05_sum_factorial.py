# Class 5 - accumulators: sum and factorial

n = int(input("n: "))
total = 0      # 0 for adding
fact = 1       # 1 for multiplying
for i in range(1, n + 1):
    total += i
    fact *= i
print("Sum =", total)
print("Factorial =", fact)
