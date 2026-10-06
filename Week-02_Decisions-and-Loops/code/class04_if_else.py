# Class 4 - if and else (slides: if, else)

# Pass or not: the indented line runs only when the condition is True
marks = int(input("Marks: "))
if marks >= 40:
    print("Pass! Well done")
print("Result checked")

# Even or odd
n = int(input("Number: "))
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

# Can you vote?
age = int(input("Age: "))
if age >= 18:
    print("You can vote")
else:
    print("Wait", 18 - age, "years")
