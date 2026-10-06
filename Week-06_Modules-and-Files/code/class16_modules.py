# Class 16 - modules: math, random, datetime

import math
import random
from datetime import date

print(math.sqrt(81), math.pow(2, 5))         # 9.0 32.0
print(math.ceil(4.2), math.floor(4.8))       # 5 4
print(math.factorial(5), math.gcd(48, 18))   # 120 6
print(round(math.pi, 2))                     # 3.14
print("Benches for 47 students:", math.ceil(47 / 6))   # 8

dice = random.randint(1, 6)                  # 1 to 6, both included
otp = random.randint(1000, 9999)
snack = random.choice(["Samosa", "Bara", "Gupchup"])
names = ["Ananya", "Subham", "Priyanka"]
random.shuffle(names)
print(dice, otp, snack)
print(names)

today = date.today()
print("Today:", today)
exam = date(2026, 12, 15)                    # put the real exam date here
print("Days to exam:", (exam - today).days)
print(today.strftime("%d/%m/%Y"))
