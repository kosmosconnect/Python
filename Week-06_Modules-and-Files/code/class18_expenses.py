# Class 18 - Mini-project 2: expense tracker saved to expenses.csv
# One row per expense: date, category, amount, note

import csv
import os
from datetime import date

FILE = "expenses.csv"


def load():
    data = []
    if os.path.exists(FILE):
        with open(FILE) as f:
            for row in csv.reader(f):
                data.append(row)
    return data


def add(data):
    amt = input("Amount: Rs. ")
    cat = input("Category: ").strip().title()
    note = input("Note: ")
    row = [str(date.today()), cat, amt, note]
    data.append(row)
    with open(FILE, "a", newline="") as f:
        csv.writer(f).writerow(row)
    print("Saved.")


def show(data):
    running = 0
    for d, cat, amt, note in data:
        running += float(amt)
        print(f"{d}  {cat:8} Rs. {float(amt):8.2f}  {note}")
    print(f"Total so far: Rs. {running:.2f}")


def report(data):
    t = {}
    for d, cat, amt, note in data:
        t[cat] = t.get(cat, 0) + float(amt)
    for cat, total in sorted(t.items()):
        print(f"{cat:10} Rs. {total:8.2f}")
    print("Total:", sum(t.values()))


def main():
    data = load()
    print(len(data), "expenses loaded from", FILE)
    while True:
        print("\n1 Add  2 Show  3 Report  0 Exit")
        choice = input("Choice: ")
        if choice == "1":
            add(data)
        elif choice == "2":
            show(data)
        elif choice == "3":
            report(data)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice")


main()
