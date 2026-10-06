# Class 13 practice - answers

# Task 1: Circle
def area(r):
    return 3.14159 * r * r

def perimeter(r):
    return 2 * 3.14159 * r

print(f"{area(7):.2f} {perimeter(7):.2f}")      # 153.94 43.98

# Task 2: Max of three without max()
def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c

print(biggest(12, 45, 27))                     # 45

# Task 3: Factorial with a loop
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for i in range(1, 7):
    print(f"{i}! = {fact(i)}")

# Task 4: Vowel count
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

for w in ["Konark", "Odisha", "Bhubaneswar"]:
    print(w, count_vowels(w))
