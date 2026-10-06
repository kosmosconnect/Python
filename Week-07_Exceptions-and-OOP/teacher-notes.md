# Python Week 7 – Exceptions & OOP: teacher notes

## Week 7 cover

### Slide 1: Errors and objects

Week 7 has two big ideas. Classes: (19) exceptions, so bad input or a missing file no longer crashes the program; (20) classes and objects; (21) inheritance and the four pillars of OOP. OOP is a major part of the first-year syllabus and viva. Check the Week 6 expense tracker first: typing "abc" as the amount crashes it, which is today's motivation.

## Class 19 — errors, exceptions, try/except, else, finally, raise

### Slide 2: Handling errors

Warm-up: run the expense tracker and type "abc" as the amount, or 10 / 0 in the shell. A red traceback appears and the program dies. Real apps never do that to users: they show a message and carry on. Show the student how to read a traceback: the LAST line names the error type and message, the line above shows where it happened.

### Slide 3: Three kinds of mistakes

Syntax errors are caught by Python before any line runs (SyntaxError, IndentationError). Exceptions happen at run time and are what try/except handles. Logic errors are the hardest: in avg = a + b / 2 the division happens first (BODMAS from Week 1), so the answer is wrong but there is no error message. The fix is (a + b) / 2. Viva: what is an exception? (An error detected during execution that can be handled.)

### Slide 4: Exceptions you will meet

Trigger each one live in the shell and read the last line together. The student should be able to say why each happens: ValueError, right type but bad value; TypeError, wrong type for the operation; IndexError, position out of range; KeyError, missing dictionary key; NameError, variable never created (often a typo, or used before assignment). This list is popular in viva questions.

### Slide 5: Catching an error

Run it twice: with 19 (the except block is skipped) and with nineteen (the int() line fails, Python jumps straight to except, and the print inside try never runs). Name the exception you expect: a bare except: catches everything, even typing mistakes in your own code, which hides bugs. Keep the try block small: only the lines that can fail.

### Slide 6: Several excepts, else and finally

Test three inputs: 10 and 2 (else runs: Answer 5.0, then Done), 10 and 0 (ZeroDivisionError branch, then Done), and 10 and x (ValueError branch, then Done). finally is for clean-up that must always happen. You can catch the error object to show Python's own message: except ValueError as e: print("Problem:", e). Order of blocks is fixed: try, except(s), else, finally.

### Slide 7: Keep asking until the input is valid

This combines Week 2 (while True), Week 5 (functions and return) and today. return exits both the loop and the function as soon as a valid number arrives. Ask the student to extend it: get_int(prompt, low, high) that also rejects numbers outside a range, for example marks between 0 and 100. That version is in the code folder.

### Slide 8: Raising your own errors

Functions should refuse bad requests instead of returning nonsense. Here the function only checks; the caller decides whether to print a message, ask again or stop. Try withdraw(500, -50) and withdraw(500, 200) (gives 300). This leads straight into tomorrow's BankAccount class, where withdraw becomes a method.

### Slide 9: Your turn: four safe programs

Answers are in solutions/class19_practice.py. Hints. Task 1: the divide.py slide. Task 2: inside the loop, after converting, if low <= n <= high: return n, else print a message. Task 3: wrap the with open block in try / except FileNotFoundError. Task 4: replace amt = input(...) with a float version of get_int.

## Class 20 — classes, objects, __init__, self, methods and __str__

### Slide 10: Classes and objects

Warm-up: in the record manager, a student was a name plus a list of marks, and the functions lived separately. What if a student could carry its own data AND its own actions, like s.average()? That is object-oriented programming. We have been using objects all along: a string is an object, and "hi".upper() is calling a method on it.

### Slide 11: A class is a blueprint, an object is the real thing

Use a familiar class: the Student class at ITER. The class says every student has a name, roll number and marks, and can calculate their average. Ananya and Subham are two objects (instances) made from it, each with their own values. Another example: Car is a class; your uncle's white Swift is an object. Viva: define class and object. (A class is a user-defined blueprint; an object is an instance of a class.)

### Slide 12: A Student class

__init__ (two underscores each side, "dunder init") is the constructor: it sets up the new object's attributes. Student("Ananya", [...]) creates an object and calls __init__ with those values. s1 and s2 have separate name and marks. Methods are functions defined inside a class; the first parameter is always self. Common errors: forgetting self in the method definition, or writing init with single underscores.

### Slide 13: What is self?

This is the most confusing part of OOP for beginners, so slow down. Write on the board: s1.average() is the same as Student.average(s1). Run both forms to prove it. self is just the name of the first parameter; it is a convention, not a keyword, but always use it. self.name = name means "store the name in THIS object". Without self, name would be a local variable that disappears when __init__ ends (Week 5 scope).

### Slide 14: A bank account object

Trace: 1000, deposit 500 gives 1500, withdraw 300 gives 1200. Make a second account to show objects are independent: acc2 = Account("Rahul"), whose balance starts at the default 0. Try acc.withdraw(5000) inside try/except. This is the standard lab program for classes (sometimes with a menu: deposit, withdraw, check balance, exit), and it is the base for Practice task 2.

### Slide 15: Printing an object nicely

__str__ must RETURN a string, not print it. It is called automatically by print() and str(). This is a first taste of "special methods" (dunder methods); others like __len__ and __eq__ exist but are not needed now. Ask the student to add __str__ to the Account class so print(acc) shows "Priyanka: Rs. 1200".

### Slide 16: Your turn: four programs

Answers are in solutions/class20_practice.py. Hints. Task 1: return self.length * self.breadth. Task 2: the Week 4 menu loop calling acc.deposit(...), with try/except around withdraw. Task 3: self.price -= self.price * percent / 100. Task 4: loop through the list keeping the student with the highest average(), or max(students, key=lambda s: s.average()).

## Class 21 — inheritance, super(), polymorphism and the four pillars

### Slide 17: Inheritance

Warm-up: write a tiny class Person with name and a greet() method. Today: a Student is a Person, and a Teacher is a Person. Instead of copying name and greet into both, they inherit them. Children inherit features from parents: the analogy writes itself. Finish with the four OOP pillars, a guaranteed viva question.

### Slide 18: A Student is a Person

The brackets in class Student(Person) mean "Student inherits from Person". Student has no __init__ or greet of its own, yet s.greet() works: Python looks in Student, does not find it, and moves up to Person. This is an "is-a" relationship: a Student is a Person. Ask: is a Person a Student? (No: p = Person("X"); p.study() is an AttributeError.) Viva: types of inheritance: single, multiple, multilevel, hierarchical (name them; single is enough for code).

### Slide 19: Adding new data in the child

super() means "my parent class". Without the super().__init__(name) line, self.name would never be set and greet would crash with AttributeError: let the student delete it and see. Method overriding: when the child defines a method with the same name, the child's version wins. Calling super().greet() inside it reuses the parent's work instead of copying it.

### Slide 20: Same method name, different behaviour

Polymorphism means code can treat different objects the same way, as long as they have the same method. The loop does not care whether s is a rectangle or a circle. In bigger programs both classes would inherit from a Shape parent with its own area(). Built-in example: len() works on strings, lists and dictionaries, and + adds numbers but joins strings. Ask the student to add a Triangle class and put it in the list.

### Slide 21: The four pillars of OOP (viva favourite)

Make the student say each pillar with its example from this week, without looking. Encapsulation also covers hiding data: by convention an attribute starting with an underscore (self._balance) means "internal, do not touch from outside"; two underscores (self.__balance) make Python rename it so it is harder to reach. Abstraction is like driving a car: you use the steering and brakes without knowing how the engine works. These definitions are worth memorising for the viva.

### Slide 22: Your turn: four programs

Answers are in solutions/class21_practice.py. Hints. Task 1: copy the super() slide, with subject instead of branch. Task 2: self.balance += self.balance * rate / 100, using the Account class from Class 20. Task 3: 0.5 * base * height and side * side. Task 4: Vehicle.wheels returns 0, Bike returns 2, Car returns 4.

## Week 7 recap and what comes next

### Slide 23: What you can do now

Oral quiz: 1. Syntax error vs exception? 2. Name four built-in exceptions. 3. When does else run? finally? 4. Class vs object? 5. What is __init__? 6. What is self? 7. What does super() do? 8. Name the four pillars with an example each. Next week is the capstone: ask the student to choose between a Library system and an ATM system before the next class.
