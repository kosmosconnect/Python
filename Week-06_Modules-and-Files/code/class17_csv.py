# Class 17 - CSV files

import csv

rows = [["Ananya", 92], ["Ravi", 78]]
with open("marks.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Marks"])
    w.writerows(rows)

with open("marks.csv") as f:
    for row in csv.reader(f):
        print(row)
