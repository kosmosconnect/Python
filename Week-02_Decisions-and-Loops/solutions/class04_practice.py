# Class 4 practice - answers

# Task 1: Sign check
n = int(input("Number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Task 2: Triangle type
a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

# Task 3: Electricity bill (first 100 units Rs. 5, the rest Rs. 7)
units = int(input("Units: "))
if units <= 100:
    bill = units * 5
else:
    bill = 100 * 5 + (units - 100) * 7
print("Bill: Rs.", bill)              # 150 units -> Rs. 850

# Task 4: Mini calculator
x = float(input("First number: "))
y = float(input("Second number: "))
op = input("Operator (+ - * /): ")
if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    if y == 0:
        print("Cannot divide by zero")
    else:
        print(x / y)
else:
    print("Unknown operator")
