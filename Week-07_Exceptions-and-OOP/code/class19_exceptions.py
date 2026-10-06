# Class 19 - handling errors

# try / except
try:
    age = int(input("Age: "))
    print("Next year you will be", age + 1)
except ValueError:
    print("Please type a number, like 19")
print("Program continues")

# several excepts, else and finally
try:
    a = int(input("a: "))
    b = int(input("b: "))
    result = a / b
except ValueError:
    print("Numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Answer:", result)
finally:
    print("Done")


# keep asking until the input is valid (optionally within a range)
def get_int(prompt, low=None, high=None):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            print("Not a number, try again")
            continue
        if (low is None or n >= low) and (high is None or n <= high):
            return n
        print(f"Please enter a number from {low} to {high}")

marks = get_int("Marks (0-100): ", 0, 100)
print("Saved", marks)


# raising your own errors
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be > 0")
    if amount > balance:
        raise ValueError("Not enough balance")
    return balance - amount

try:
    print(withdraw(500, 800))
except ValueError as e:
    print("Error:", e)
