# Class 2 - input() and type casting (slides: "input()", "The input() trap")

# input() shows a message, waits for Enter, and ALWAYS gives back a string
name = input("Enter your name: ")
city = input("Your city: ")
print("Hello", name, "from", city)

# The trap: this line would crash with a TypeError, because "18" + 1 is not allowed
# age = input("Age: ")
# print(age + 1)

# The fix: convert the string to a number first
age = int(input("Age: "))
print(age + 1)

# Casting cheat sheet
print(int("25"))      # 25
print(float("8.5"))   # 8.5
print(str(100))       # "100" (prints as 100)
print(int(9.99))      # 9  - int() chops the decimal, it does not round
