# Class 20 - classes and objects

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.name}: {self.marks}"

s1 = Student("Ananya", [78, 85, 92])
s2 = Student("Subham", [65, 70, 88])
print(s1.name, s1.average())               # Ananya 85.0
print(s2.name, round(s2.average(), 1))     # Subham 74.3
print(Student.average(s1))                 # same as s1.average()
print(s1)                                  # uses __str__


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

    def __str__(self):
        return f"{self.owner}: Rs. {self.balance}"

acc = Account("Priyanka", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.owner, acc.balance)              # Priyanka 1200
try:
    acc.withdraw(5000)
except ValueError as e:
    print("Error:", e)
print(acc)
