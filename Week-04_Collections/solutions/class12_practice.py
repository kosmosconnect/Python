# Class 12 practice - extensions to the record manager
# Each piece below goes into class12_records.py. Sample data to test with:

students = {"Ananya": [78, 85, 92], "Subham": [65, 70, 38], "Priyanka": [88, 91, 79]}

# Task 1: Grades next to the average
for name, m in students.items():
    avg = sum(m) / 3
    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "F"
    print(name, m, f"{avg:.1f}", grade)

# Task 2: Delete (choice 5)
name = input("Delete who? ").strip().title()
if name in students:
    students.pop(name)
    print("Deleted", name)
else:
    print("Not found")

# Task 3: Average of each subject
SUBJECTS = ["Maths", "Physics", "Python"]
for i in range(3):
    total = 0
    for m in students.values():
        total += m[i]
    print(SUBJECTS[i], f"{total / len(students):.1f}")

# Task 4: Fail list
for name, m in students.items():
    if min(m) < 40:
        print(name, "needs help:", m)
