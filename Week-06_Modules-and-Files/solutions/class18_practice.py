# Class 18 practice - extensions for the expense tracker
# Uses the same file as code/class18_expenses.py

import csv
import os
from datetime import date

FILE = "expenses.csv"
BUDGET = 3000

data = []
if os.path.exists(FILE):
    with open(FILE) as f:
        data = [row for row in csv.reader(f)]

# Task 1: This month only
month = str(date.today())[:7]               # e.g. "2026-10"
this_month = [r for r in data if r[0][:7] == month]
spent = sum(float(r[2]) for r in this_month)
print(f"This month: {len(this_month)} expenses, Rs. {spent:.2f}")

# Task 2: Biggest single spend
if data:
    big = data[0]
    for r in data:
        if float(r[2]) > float(big[2]):
            big = r
    print("Biggest:", big[2], "on", big[3])

# Task 3: Budget alert
if spent > BUDGET:
    print("Over budget by Rs.", spent - BUDGET)
else:
    print("Left in budget: Rs.", BUDGET - spent)

# Task 4: Delete the last expense and rewrite the file
if data and input("Delete last expense? (y/n) ") == "y":
    removed = data.pop()
    with open(FILE, "w", newline="") as f:
        csv.writer(f).writerows(data)
    print("Removed", removed)
