# Class 3 - Operators (slides: calculator, // and %, comparing, BODMAS, f-strings)

a, b = 17, 5
print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4  - / always gives a float
print(a // b)   # 3    - floor division
print(a % b)    # 2    - remainder
print(2 ** 5)   # 32   - power (not ^)

# // and % in real life
print(47 // 6, "boxes,", 47 % 6, "rasagolas left")   # 7 boxes, 5 left
print(130 // 60, "hrs", 130 % 60, "min")             # 2 hrs 10 min
print(14 % 2 == 0)                                   # True, so 14 is even

# Comparing and combining
attendance = 80
marks = 35
print(attendance >= 75)                  # True
print(attendance >= 75 and marks >= 40)  # False - both must be True
print(attendance >= 75 or marks >= 40)   # True  - one is enough

# Order of operations (BODMAS)
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
print(10 - 4 / 2)     # 8.0
print(2 ** 3 * 2)     # 16

x = 10
x += 5                # same as x = x + 5
print(x)              # 15

# f-strings
name = "Priyanka"
pct = 437 / 500 * 100
print(f"{name} scored {pct:.2f}%")   # Priyanka scored 87.40%
