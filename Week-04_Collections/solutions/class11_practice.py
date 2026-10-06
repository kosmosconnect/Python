# Class 11 practice - answers

# Task 1: Phone book
book = {}
for i in range(3):
    name = input("Name: ").strip().title()
    book[name] = input("Number: ")
look = input("Search: ").strip().title()
print(book.get(look, "Not found"))

# Task 2: Common friends
mine = ["Ananya", "Subham", "Priyanka", "Rahul"]
yours = ["Rahul", "Sneha", "Ananya"]
a, b = set(mine), set(yours)
print("Both:", a & b)
print("Only one:", a ^ b)

# Task 3: Word count
line = "to be or not to be"
count = {}
for w in line.split():
    count[w] = count.get(w, 0) + 1
print(count)                       # {'to': 2, 'be': 2, 'or': 1, 'not': 1}

# Task 4: Topper and class average
marks = {"Ananya": 92, "Subham": 78, "Priyanka": 88}
best = ""
for name, m in marks.items():
    if best == "" or m > marks[best]:
        best = name
print("Topper:", best, marks[best])
print(f"Average: {sum(marks.values()) / len(marks):.1f}")
