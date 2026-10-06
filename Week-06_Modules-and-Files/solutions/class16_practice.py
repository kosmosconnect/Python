# Class 16 practice - answers

import math
import random
from datetime import date

# Task 1: Guess the number
secret = random.randint(1, 50)
tries = 0
while True:
    guess = int(input("Guess (1-50): "))
    tries += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! Tries:", tries)
        break

# Task 2: Benches
students = int(input("Students: "))
per_bench = int(input("Seats per bench: "))
print("Benches needed:", math.ceil(students / per_bench))

# Task 3: Age this year
born = int(input("Birth year: "))
print("Age this year:", date.today().year - born)

# Task 4: OTP
otp = random.randint(100000, 999999)
print("Your OTP is", otp)
if input("Type the OTP: ") == str(otp):
    print("Verified")
else:
    print("Wrong OTP")
