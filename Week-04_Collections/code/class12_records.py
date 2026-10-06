# Class 12 - Mini-project 1: student record manager
# Data: {name: [maths, physics, python]}

students = {}
SUBJECTS = ["Maths", "Physics", "Python"]
MENU = "1 Add  2 Show  3 Find  4 Top  0 Exit"

while True:
    print()
    print(MENU)
    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ").strip().title()
        marks = []
        for sub in SUBJECTS:
            marks.append(int(input(sub + ": ")))
        students[name] = marks
        print("Saved", name)

    elif choice == "2":
        if not students:
            print("No students yet")
        for name, m in students.items():
            print(name, m, f"{sum(m) / 3:.1f}")

    elif choice == "3":
        name = input("Find: ").strip().title()
        if name in students:
            print(name, students[name])
        else:
            print("Not found")

    elif choice == "4":
        best, best_total = "", -1
        for name, m in students.items():
            if sum(m) > best_total:
                best, best_total = name, sum(m)
        if best:
            print("Topper:", best, best_total)
        else:
            print("No students yet")

    elif choice == "0":
        print("Bye!")
        break

    else:
        print("Invalid choice")
