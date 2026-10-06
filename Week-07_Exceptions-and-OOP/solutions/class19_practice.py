# Class 19 practice - answers

# Task 1: Safe division
try:
    a = float(input("a: "))
    b = float(input("b: "))
    print("Answer:", a / b)
except ValueError:
    print("Numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Task 2: get_int with a range
def get_int(prompt, low, high):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            print("Not a number")
            continue
        if low <= n <= high:
            return n
        print(f"Must be between {low} and {high}")

print("You chose", get_int("Pick 1-10: ", 1, 10))

# Task 3: Safe file open
name = input("File name: ")
try:
    with open(name) as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Sorry, no file called", name)

# Task 4: a safe amount for the expense tracker
def get_amount(prompt):
    while True:
        try:
            amt = float(input(prompt))
            if amt > 0:
                return amt
            print("Amount must be more than 0")
        except ValueError:
            print("Please type a number like 40 or 12.50")

print("Amount saved:", get_amount("Amount: Rs. "))
