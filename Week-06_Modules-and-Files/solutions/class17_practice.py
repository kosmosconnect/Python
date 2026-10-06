# Class 17 practice - answers

import csv
import os
from datetime import date

# Sample files from class17_files.py and class17_csv.py, in case they were run in another folder
if not os.path.exists("cities.txt"):
    with open("cities.txt", "w") as f:
        f.write("Bhubaneswar\nCuttack\nPuri\nKonark\n")
if not os.path.exists("marks.csv"):
    with open("marks.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Marks"], ["Ananya", 92], ["Ravi", 78]])

# Task 1: Diary - one new line per run
text = input("Today's line: ")
with open("diary.txt", "a") as f:
    f.write(f"{date.today()}: {text}\n")

# Task 2: Search a file
word = input("Search for: ")
with open("cities.txt") as f:
    for line in f:
        if word.lower() in line.lower():
            print(line.strip())

# Task 3: Average from marks.csv
total = count = 0
with open("marks.csv") as f:
    reader = csv.reader(f)
    next(reader)                      # skip the header row
    for row in reader:
        total += int(row[1])
        count += 1
print("Class average:", total / count)

# Task 4: Copy in capitals
with open("cities.txt") as src, open("cities_upper.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())
print("Copied to cities_upper.txt")
