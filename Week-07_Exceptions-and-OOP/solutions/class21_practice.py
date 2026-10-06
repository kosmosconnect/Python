# Class 21 practice - answers

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Namaskar, I am", self.name)


# Task 1: Teacher
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def greet(self):
        super().greet()
        print("I teach", self.subject)

Teacher("Mr. Mishra", "Python").greet()


# Task 2: SavingsAccount
class Account:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance

class SavingsAccount(Account):
    def add_interest(self, rate):
        self.balance += self.balance * rate / 100

sa = SavingsAccount("Ananya", 10000)
sa.add_interest(4)
print(sa.balance)                       # 10400.0


# Task 3: more shapes
class Triangle:
    def __init__(self, base, height):
        self.base, self.height = base, height

    def area(self):
        return 0.5 * self.base * self.height

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

for shape in [Triangle(6, 4), Square(3)]:
    print(type(shape).__name__, shape.area())


# Task 4: vehicles
class Vehicle:
    def wheels(self):
        return 0

class Bike(Vehicle):
    def wheels(self):
        return 2

class Car(Vehicle):
    def wheels(self):
        return 4

for v in [Bike(), Car()]:
    print(type(v).__name__, v.wheels())
