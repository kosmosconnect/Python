# Class 21 - inheritance, super() and polymorphism

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Namaskar, I am", self.name)


class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)             # let Person set the name
        self.branch = branch

    def greet(self):                       # overrides Person.greet
        super().greet()
        print("I study", self.branch)

    def study(self):
        print(self.name, "is coding")


p = Person("Rahul")
p.greet()
s = Student("Ananya", "CSE")
s.greet()
s.study()


class Rectangle:
    def __init__(self, l, b):
        self.l, self.b = l, b

    def area(self):
        return self.l * self.b


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2


for shape in [Rectangle(4, 5), Circle(1)]:
    print(type(shape).__name__, round(shape.area(), 2))
