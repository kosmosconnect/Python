# Class 3 practice - answers

# Task 1: Circle
pi = 3.14159
r = float(input("Radius: "))
print(f"Area = {pi * r * r:.2f}")
print(f"Circumference = {2 * pi * r:.2f}")

# Task 2: Temperature
c = float(input("Celsius: "))
f = c * 9 / 5 + 32
print(f"{c} C = {f:.1f} F")          # 37 -> 98.6

# Task 3: Swap - the Python way and the classic way
a = int(input("a: "))
b = int(input("b: "))
a, b = b, a
print("After swap:", a, b)
temp = a                              # classic way with a third variable
a = b
b = temp
print("Swapped back:", a, b)

# Task 4: Time breaker
s = int(input("Seconds: "))          # 3725 -> 1 h 2 m 5 s
h = s // 3600
rest = s % 3600
m = rest // 60
sec = rest % 60
print(f"{h} h {m} m {sec} s")
