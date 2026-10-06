# Class 5 - taking a number apart: reverse, digit sum, palindrome

n = int(input("Number: "))
original = n
rev = 0
total = 0
while n > 0:
    d = n % 10       # last digit
    rev = rev * 10 + d
    total += d
    n //= 10         # drop it
print("Reversed:", rev)
print("Digit sum:", total)
if rev == original:
    print(original, "is a palindrome")
