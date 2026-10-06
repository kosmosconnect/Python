# Class 4 - elif ladder: the grade calculator
# Python checks top to bottom and stops at the first True.

marks = int(input("Marks: "))
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)
