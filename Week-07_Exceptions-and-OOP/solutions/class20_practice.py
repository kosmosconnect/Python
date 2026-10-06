# Class 20 practice - answers

# Task 1: Rectangle
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

r = Rectangle(4, 5)
print(r.area(), r.perimeter())          # 20 18


# Task 2: Bank menu
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt > self.balance:
            raise ValueError("Low balance")
        self.balance -= amt

acc = Account(input("Owner: "))
while True:
    choice = input("1 Deposit  2 Withdraw  3 Balance  0 Exit: ")
    try:
        if choice == "1":
            acc.deposit(float(input("Amount: ")))
        elif choice == "2":
            acc.withdraw(float(input("Amount: ")))
        elif choice == "3":
            print("Balance:", acc.balance)
        elif choice == "0":
            break
        else:
            print("Invalid choice")
    except ValueError as e:
        print("Error:", e)


# Task 3: Book
class Book:
    def __init__(self, title, author, price):
        self.title, self.author, self.price = title, author, price

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100

    def __str__(self):
        return f"{self.title} by {self.author}, Rs. {self.price:.2f}"

b = Book("Python Basics", "A. Sahoo", 450)
b.apply_discount(10)
print(b)                                # Rs. 405.00


# Task 4: list of students and the topper
class Student:
    def __init__(self, name, marks):
        self.name, self.marks = name, marks

    def average(self):
        return sum(self.marks) / len(self.marks)

students = [Student("Ananya", [78, 85, 92]), Student("Subham", [65, 70, 88]),
            Student("Priyanka", [88, 91, 79])]
top = students[0]
for s in students:
    if s.average() > top.average():
        top = s
print("Topper:", top.name, round(top.average(), 1))
