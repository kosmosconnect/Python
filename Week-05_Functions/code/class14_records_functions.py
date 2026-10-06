# Class 14 - the Week 4 record manager, rebuilt with functions
# Data: {name: [maths, physics, python]}

SUBJECTS = ["Maths", "Physics", "Python"]


def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    return "F"


def add_student(db):
    name = input("Name: ").strip().title()
    marks = []
    for sub in SUBJECTS:
        marks.append(int(input(sub + ": ")))
    db[name] = marks
    print("Saved", name)


def show_all(db):
    if not db:
        print("No students yet")
    for name, m in db.items():
        avg = sum(m) / len(m)
        print(f"{name:10} {m} {avg:5.1f} {grade(avg)}")


def find(db, name):
    return db.get(name)            # None if missing


def topper(db):
    best, best_total = None, -1
    for name, m in db.items():
        if sum(m) > best_total:
            best, best_total = name, sum(m)
    return best, best_total


def main():
    students = {}
    while True:
        print("\n1 Add  2 Show  3 Find  4 Top  0 Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            name = input("Find: ").strip().title()
            marks = find(students, name)
            print(name, marks if marks else "not found")
        elif choice == "4":
            name, total = topper(students)
            print("Topper:", name, total)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice")


main()
