# Class 15 - recursion

def fact(n):
    if n <= 1:                   # base case (also makes 0! = 1)
        return 1
    return n * fact(n - 1)       # recursive case

print(fact(5))                   # 120

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(8)])   # [0, 1, 1, 2, 3, 5, 8, 13]

def dsum(n):
    if n < 10:
        return n
    return n % 10 + dsum(n // 10)

print(dsum(1234))                # 10

# Bonus: Tower of Hanoi with 3 discs
def hanoi(n, a, b, c):
    if n:
        hanoi(n - 1, a, c, b)
        print(a, "->", c)
        hanoi(n - 1, b, a, c)

hanoi(3, "A", "B", "C")
