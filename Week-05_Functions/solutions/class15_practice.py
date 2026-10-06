# Class 15 practice - answers (base case first, then the recursive case)

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

def rev(s):
    if len(s) <= 1:
        return s
    return s[-1] + rev(s[:-1])

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(power(2, 10))      # 1024
print(total(10))         # 55
print(rev("Konark"))     # kranoK
print(gcd(48, 18))       # 6
